
import pytest

from warranty_claims import (
    out_of_warranty_charge,
    claim_allowed,
    sla_status
)


# --------------------------------------------------
# TESTS FOR out_of_warranty_charge()
# --------------------------------------------------

def test_unknown_plan():
    with pytest.raises(ValueError):
        out_of_warranty_charge("gold", 10, "defect", False)


def test_negative_age():
    with pytest.raises(ValueError):
        out_of_warranty_charge("basic", -1, "defect", False)


def test_within_warranty():
    assert out_of_warranty_charge(
        "standard", 20, "defect", False
    ) == 0


def test_registered_customer_extra_coverage():
    assert out_of_warranty_charge(
        "basic", 15, "defect", True
    ) == 0


def test_accidental_claim_within_12_months():
    assert out_of_warranty_charge(
        "basic", 13, "accidental", False
    ) == 200


def test_defect_claim_within_12_months():
    assert out_of_warranty_charge(
        "basic", 13, "defect", False
    ) == 100


def test_defect_claim_exceeding_12_months():
    assert out_of_warranty_charge(
        "basic", 25, "defect", False
    ) == 1950


def test_accidental_claim_exceeding_12_months():
    assert out_of_warranty_charge(
        "basic", 25, "accidental", False
    ) == 3575


# --------------------------------------------------
# TESTS FOR claim_allowed()
# --------------------------------------------------

def test_recall_claim_within_limit():
    assert claim_allowed(10, 5, True) is True


def test_recall_claim_exceeding_limit():
    assert claim_allowed(10, 6, True) is False


def test_claim_within_30_days():
    assert claim_allowed(20, 1, False) is False


def test_claim_after_30_days_within_limit():
    assert claim_allowed(60, 2, False) is True


def test_claim_after_30_days_exceeding_limit():
    assert claim_allowed(60, 3, False) is False


# --------------------------------------------------
# TESTS FOR sla_status()
# --------------------------------------------------

def test_hardware_on_track():
    assert sla_status(60, True, False) == "on_track"


def test_software_on_track():
    assert sla_status(30, False, False) == "on_track"


def test_priority_hardware_on_track():
    assert sla_status(80, True, True) == "on_track"


def test_hardware_at_risk():
    assert sla_status(40, True, False) == "at_risk"


def test_software_at_risk():
    assert sla_status(20, False, False) == "at_risk"


def test_priority_hardware_critical():
    assert sla_status(10, True, True) == "critical"
