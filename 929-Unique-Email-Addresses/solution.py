"""LeetCode Problem 929 - Unique Email Addresses

Every valid email consists of a local name and a domain name, separated by the
'@' sign. Besides lowercase letters, the email may contain one or more '.' or
'+'.

For example, in "alice@leetcode.com", "alice" is the local name, and
"leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an
email address, mail sent there will be forwarded to the same address without
dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the
same email address.
If you add a plus '+' in the local name, everything after the first plus sign
will be ignored. This allows certain emails to be filtered. Note that this rule
does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i],
return the number of different addresses that actually receive mails.

Constraints
===========
 * 1 <= emails.length <= 100
 * 1 <= emails[i].length <= 100
 * emails[i] consist of lowercase English letters, '+', '.' and '@'.
 * Each emails[i] contains exactly one '@' character.
 * All local and domain names are non-empty.
 * Local names do not start with a '+' character.
 * Domain names end with the ".com" suffix.

"""

from abc import ABC, abstractmethod
from collections import namedtuple
from copy import deepcopy
from typing import List, NewType, Set, Text

from pytest import FixtureRequest, fixture


# Define an email address to be a specific subtype of text strings.
EmailAddress = NewType("EmailAddress", Text)

# Define an email components structure as a binary tuple with the local address
# as its first component and the domain address as its second component.
EmailComponents = namedtuple("Email", ["local", "domain"])


def deconstruct_email(email: EmailAddress) -> EmailComponents:
    """Deconstruct Email"""
    # Split the email address into its local and domain constituent components
    # using the @ symbol as the split sentinel.
    local, domain = email.split("@")

    # Return the deconstructed email address as a binary tuple of its local and
    # domain address components.
    return EmailComponents(local, domain)


def reconstruct_email(address: EmailComponents) -> EmailAddress:
    """Reconstruct Email

    This function reconstructs the email address from its two constituent
    components by simply appending them together, with the requisite @ symbol
    in between.
    """
    return f"{address.local}@{address.domain}"


class AddressFilter(ABC):
    """Filter Class"""

    def __call__(self, text: Text) -> Text:
        return self.filter(text)

    @abstractmethod
    def filter(self, text: Text) -> Text:
        pass


class PlusSignSuffixFilter(AddressFilter):
    """Plus-Sign Suffix Filter

    This filter ignores all of the text in a string beyond (and including) the
    first plus sign in the string.
    """
    def filter(self, text: Text) -> Text:
        """Filter Plus Sign Suffix From Input String"""
        # Iterate over the input string using the enumeration iterator. The
        # enumerate function call allows us to have both the current index and
        # the current character during each step of the iteration.
        for index, character in enumerate(text):
            # The first plus sign and everything after it are completely
            # filtered from the input string, so we need to check whether the
            # current character in the input string is a plus sign.
            if character == "+":
                # Return a copy of the input string up to, but not including,
                # the current index, thereby completely ignoring the plus sign
                # and everything after it.
                return text[:index]

        # If there was no plus sign in the input string, there is nothing to
        # filter, and since every filter returns a copy of the input string if
        # a modification is necessary, we can safely return the text string
        # itself, since no modification was required.
        return text


class IgnoreAllPeriodsFilter(AddressFilter):
    """Ignore All Periods Filter

    This filter ignores all periods in a string, returning the input string as
    if it had no periods in it at all.
    """
    def filter(self, text: Text) -> Text:
        """Filter All Periods From Text"""
        # Do not modify the input string in-place. Instead, a new text string
        # is created.
        filtered_text = ""

        # Begin iterating over the input string.
        for character in text:
            # Check whether the current character is a period.
            if character == ".":
                # If it is, move on to the next loop iteration. In other words,
                # don't add periods to the output string.
                continue

            # If the current character is not a period, go ahead and append the
            # current character to the output string.
            filtered_text += character

        # Once the input string has been fully processed, return the filtered
        # text string.
        return filtered_text


class CompositeAddressFilter(AddressFilter):
    """Composite Address Filter"""
    def __init__(self, filters: List[AddressFilter]) -> None:
        """Initialize Address Filter Component"""
        self._filters = filters

    def filter(self, text: Text) -> Text:
        # Do not modify the text object in-place. Instead, create a deep copy
        # of the text string that will be modified instead.
        filtered_text = deepcopy(text)

        # Iterate over all of the child filters in this composite filter.
        for child_filter in self._filters:
            # For each child filter, the resulting text string is processed and
            # updated.
            filtered_text = child_filter(filtered_text)

        # Return the filtered text string.
        return filtered_text


class LocalAddressFilter(CompositeAddressFilter):
    """Local Address Filter

    This is a convenience class that defines a composite filter with the
    specifications outlined in the problem description.
    """
    def __init__(self) -> None:
        """Filter Local Address

        Note that the plus sign filter is defined first, as it will thus be
        executed first, significantly decreasing the amount of work left for
        all subsequent filters.
        """
        super().__init__([PlusSignSuffixFilter(), IgnoreAllPeriodsFilter()])


def filter_local_address(local_address: Text) -> Text:
    """Filter Local Address

    Note that the plus sign filter is defined first, as it will thus be
    executed first, significantly decreasing the amount of work left for all
    subsequent filters.
    """
    # Instantiate the local address filter using the convenience class defined
    # above.
    local_address_filter = LocalAddressFilter()

    # Filter the local address defined in the input string, and return the
    # resulting local address.
    return local_address_filter(local_address)


def filter_domain_address(domain_address: Text) -> Text:
    """Filter Domain Address

    No filtering is necessary for the domain name, so we can simply return the
    domain address as is.
    """
    return domain_address


def filter_email_address(email: EmailAddress) -> EmailAddress:
    """Filter Email Address

    This function processes the local and domain address components of the
    input email address, returning the fully-filtered email address.
    """
    # Destructure the email address into its constituent components.
    local, domain = deconstruct_email(email)

    # Create an email components object using the filtered local and domain
    # addresses of the original email.
    filtered_components = EmailComponents(
        filter_local_address(local),
        filter_domain_address(domain)
    )

    # Return the reconstructed email address after filtering each of its
    # components.
    return reconstruct_email(filtered_components)


def filter_unique_emails(emails: List[EmailAddress]) -> Set[EmailAddress]:
    """Unique Emails"""
    # Create a set of all unique emails in the input list.
    unique_emails = set()

    # Iterate over the list of emails one by one.
    for email in emails:
        # Filter each email in the input list.
        filtered_email = filter_email_address(email)

        # Once the email address has been filtered, add it to the set of unique
        # email addresses.
        unique_emails.add(filtered_email)

    # Return the set of unique email addresses.
    return unique_emails


def number_of_unique_emails(emails: List[EmailAddress]) -> int:
    """Number of Unique Emails"""
    return len(filter_unique_emails(emails))


class TestPlusSignFilter:
    """Test Suite: Plus Sign Filter"""

    @fixture
    def plus_sign_filter(self) -> PlusSignSuffixFilter():
        """Fixture: Plus Sign Suffix Filter

        This fixture returns a text filter that ignores all of the characters
        in a text string beyond (and including) the first plus sign.
        """
        return PlusSignSuffixFilter()

    def test_plus_sign_filter(self, plus_sign_filter: FixtureRequest) -> None:
        """Test Case: Plus-Sign Filter

        Ensure that the plus sign filter correctly returns a string ignoring
        the first plus sign, as well as anything and everything that might have
        come after it.
        """
        assert plus_sign_filter("test.email.alex") == "test.email.alex"
        assert plus_sign_filter("test.email+alex") == "test.email"


class TestPeriodFilter:
    """Test Suite: Periods Filter"""

    @fixture
    def period_filter(self) -> IgnoreAllPeriodsFilter():
        """Fixture: Periods Filter

        This fixture returns a text filter that ignores all of the periods in a
        text string.
        """
        return IgnoreAllPeriodsFilter()

    def test_ignore_period_filter(self, period_filter: FixtureRequest) -> None:
        """Test Case: Periods Filter

        Ensure that all periods in the local address component of the email
        address are ignored.
        """
        assert period_filter("test.email+alex") == "testemail+alex"


class TestLocalAddressFilter:
    """Test Suite: Filter Local Address"""
    def test_filter_local_address(self) -> None:
        """Test Case: Local Address Filter"""
        assert filter_local_address("test.email+alex") == "testemail"


class TestDomainAddressFilter:
    """Test Suite: Filter Domain Address"""
    pass


class TestUniqueAddressFilter:
    """Test Suite: Unique Address Filter"""

    @fixture
    def example_one_email_list(self) -> List[EmailAddress]:
        return [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"
        ]

    def test_example_one(self, example_one_email_list: FixtureRequest) -> None:
        """Test Case: Example One"""
        assert number_of_unique_emails(example_one_email_list) == 2

    @fixture
    def example_two_email_list(self) -> List[EmailAddress]:
        return [
            "a@leetcode.com",
            "b@leetcode.com",
            "c@leetcode.com"
        ]

    def test_example_two(self, example_two_email_list: FixtureRequest) -> None:
        """Test Case: Example Two"""
        assert number_of_unique_emails(example_two_email_list) == 3
