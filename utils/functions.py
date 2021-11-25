from core.models import Report, UserProfile, Review
from django.contrib.auth.models import User


def report(
    owner: User,
    review: Review = None,
    userprofile: UserProfile = None
    ):
    """
    Report a review.
    """
    report, created = Report.objects.get_or_create(
        owner=owner,
        review=review,
        profile=userprofile
    )
    return report
