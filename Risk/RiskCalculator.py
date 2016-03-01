#!/usr/bin/python

"""
risk = (Vulnerability X threat) / Countermeasure Score

This program was developed on the idea of the risk formula and developed on the basis of Mathematical theory that was
pulled from The National Vulnerability Database.

Code written by Michael Kelley @ SecureSet February 2016
"""

import math

def formula():
    ISCBASE = ((ImpactC + ImpactI + ImpactA) / 3)
    print("Your ISCbase score is: %i" % ISCBASE)
    Exploitability = (((ISCBASE * (AttackVector + AttackComplexity)) - (PrivilegeRequired + UserInteraction)) / 20)
    print("Your Exploitability Score is: %i" % Exploitability)
    Temporal = ((((ISCBASE + ExploitCode) / 2) + ((RemediationLevel + ReportConfidence) / 2)) / 2)
    print("Your Temporal score is: %i" % Temporal)
    Environment = ((((CollateralDamage + Target) / 2) + ISCBASE) / 2)
    print("Your Environment score is: %i" % Environment)
    Overall = ((ISCBASE + Exploitability + Temporal + Environment)/4)
    print("Your Overall score is: %i:" % Overall)


if __name__ == '__main__':
    print('Please rate risk on a scale of one to ten:')
    ImpactC = int(input('Please rate your estimated impact to Confidentiality:'))
    ImpactI = int(input('Please rate your estimated impact to Integrity:'))
    ImpactA = int(input('Please rate your estimated impact to Availability:'))
    AttackVector = int(input('Please rate the Attack Vector:'))
    AttackComplexity = int(input('Please rate the Attack Complexity:'))
    PrivilegeRequired = int(input('Please rate the Privilege Required:'))
    UserInteraction = int(input('Please rate the level of user interaction:'))
    ExploitCode = int(input('Please rate the Maturity of the Exploitation Code:'))
    RemediationLevel = int(input('Please rate your ability to remediate:'))
    ReportConfidence = int(input('Please rate your Report Confidence:'))
    CollateralDamage = int(input('Please Rate the Potential of Collateral Damage:'))
    Target = int(input('Please rate the potential level of Target Distribution:'))

    print('Based on your inputs, your scores are as follows:')
    formula()
