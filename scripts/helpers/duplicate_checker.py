"""
Duplicate checker for member records.
"""

import logging
from typing import Dict, Optional, Tuple, Any

logger = logging.getLogger(__name__)


class DuplicateChecker:
    """Check for duplicate members by email."""

    def __init__(self, api_client, member_api):
        """
        Initialize duplicate checker.

        Args:
            api_client: Configured API client
            member_api: MemberApi instance
        """
        self.api_client = api_client
        self.member_api = member_api
        self.email_to_member: Dict[str, Dict[str, Any]] = {}
        self._loaded = False

    def load_existing_members(self) -> None:
        """
        Load existing members from the API and build email cache.
        """
        logger.info("Loading existing members from API...")

        try:
            page = 1
            total_loaded = 0

            while True:
                # Request plain JSON to avoid @context fields that the model rejects
                response = self.member_api.api_members_get_collection(
                    page=page,
                    _headers={'Accept': 'application/json'},
                )

                # Extract members from response
                # The response structure is ApiMembersGetCollection200Response
                if hasattr(response, 'hydra_member'):
                    members = response.hydra_member
                elif hasattr(response, 'member'):
                    members = response.member
                else:
                    # Try to get members from the response object
                    members = []
                    if hasattr(response, '__dict__'):
                        for key, value in response.__dict__.items():
                            if isinstance(value, list) and value:
                                members = value
                                break

                if not members:
                    break

                # Add to cache
                for member in members:
                    if hasattr(member, 'email') and member.email:
                        email_lower = member.email.lower()
                        self.email_to_member[email_lower] = {
                            'id': getattr(member, 'id', None),
                            'email': member.email,
                            'first_name': getattr(member, 'first_name', None),
                            'last_name': getattr(member, 'last_name', None),
                        }
                        total_loaded += 1

                # Check if there are more pages
                if hasattr(response, 'hydra_view') and response.hydra_view:
                    if hasattr(response.hydra_view, 'hydra_next'):
                        page += 1
                    else:
                        break
                else:
                    # No pagination info, assume single page
                    break

            self._loaded = True
            logger.info(f"Loaded {total_loaded} existing members")

        except Exception as e:
            logger.warning(f"Error loading existing members: {e}")
            logger.warning("Continuing without duplicate checking...")
            self._loaded = True  # Mark as loaded to avoid repeated attempts

    def is_duplicate(self, email: str, dry_run: bool = False) -> bool:
        """
        Check if an email already exists in the database.

        Args:
            email: Email address to check
            dry_run: If True, do not load existing members (assumes cache is already loaded)

        Returns:
            True if email exists (duplicate), False otherwise
        """
        if not self._loaded and not dry_run:
            self.load_existing_members()

        if not email:
            return False

        email_lower = email.lower()
        return email_lower in self.email_to_member

    def get_duplicate_info(self, email: str) -> Optional[Dict[str, Any]]:
        """
        Get information about the duplicate member.

        Args:
            email: Email address to look up

        Returns:
            Dictionary with member info or None if not found
        """
        if not self._loaded:
            self.load_existing_members()

        if not email:
            return None

        email_lower = email.lower()
        return self.email_to_member.get(email_lower)

    def refresh(self) -> None:
        """Refresh the member cache by reloading from API."""
        self.email_to_member.clear()
        self._loaded = False
        self.load_existing_members()

