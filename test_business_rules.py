from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    require_review,
)


def test_requires_review_over():
    assert require_review(1500) is True


def test_requires_review_under():
    assert require_review(500) is False


def test_boundary_limit():
    # exactly 1000 should NOT require review because it is (> not >=)
    assert require_review(1000) is False


def test_tier_auto():
    assert get_approval_tier(400) == "auto"


def test_tier_boundary_500():
    assert get_approval_tier(500) == "auto"


def test_tier_manager():
    assert get_approval_tier(1500) == "manager"


def test_tier_director():
    assert get_approval_tier(100000) == "director"


def test_discount_ten():
    assert apply_discount(100.00, 10) == 90.0


def test_total_includes_tax():
    assert round(calculate_total(100.00, 2), 2) == 214.00
