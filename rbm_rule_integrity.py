"""
RBM Rule Integrity Tester
Version 1.0.0

Purpose:
Compare an original human rule with its software implementation,
observed behavior, and actual result.

No external packages are required.
"""

from datetime import datetime


class RBMRuleIntegrity:
    VALUES = {
        "self_sacrifice": "Self-Sacrifice",
        "love": "Love",
        "affection": "Affection",
        "reconciliation": "Reconciliation",
        "progress": "Progress",
        "goodwill": "Goodwill",
        "freedom_of_thought": "Freedom of Thought",
        "no_coercion": "No Coercion",
        "self_respect": "Self-Respect",
        "uplift_for_good": "Uplift Others for Good Actions",
    }

    def __init__(self):
        self.reports = []

    def check(self, original_rule, software_rule, behavior, result, values):
        failed = [
            self.VALUES[key]
            for key in self.VALUES
            if values.get(key) is False
        ]

        unknown = [
            self.VALUES[key]
            for key in self.VALUES
            if values.get(key) is None
        ]

        if failed:
            status = "VIOLATION"
        elif unknown:
            status = "REVIEW"
        else:
            status = "ALIGNED"

        report = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "original_rule": original_rule,
            "software_rule": software_rule,
            "behavior": behavior,
            "result": result,
            "status": status,
            "failed_values": failed,
            "unknown_values": unknown,
            "values": {
                self.VALUES[key]: values.get(key)
                for key in self.VALUES
            },
        }

        self.reports.append(report)
        return report

    @staticmethod
    def print_report(report):
        print("\n" + "=" * 60)
        print("RBM RULE INTEGRITY REPORT")
        print("=" * 60)
        print("TIME   :", report["time"])
        print("STATUS :", report["status"])

        print("\nORIGINAL RULE")
        print(report["original_rule"])

        print("\nSOFTWARE RULE")
        print(report["software_rule"])

        print("\nOBSERVED BEHAVIOR")
        print(report["behavior"])

        print("\nACTUAL RESULT")
        print(report["result"])

        print("\nVALUE CHECK")
        for name, value in report["values"].items():
            if value is True:
                state = "PASS"
            elif value is False:
                state = "FAIL"
            else:
                state = "UNKNOWN"
            print(f"- {name}: {state}")

        if report["failed_values"]:
            print("\nFAILED VALUES")
            for value in report["failed_values"]:
                print("-", value)

        if report["unknown_values"]:
            print("\nUNKNOWN VALUES")
            for value in report["unknown_values"]:
                print("-", value)

        print("=" * 60)

    def save_report(self, report, filename="rbm_rule_report.txt"):
        with open(filename, "a", encoding="utf-8") as file:
            file.write("=" * 60 + "\n")
            file.write("RBM RULE INTEGRITY REPORT\n")
            file.write("=" * 60 + "\n")
            file.write(f"TIME: {report['time']}\n")
            file.write(f"STATUS: {report['status']}\n")
            file.write(f"ORIGINAL RULE: {report['original_rule']}\n")
            file.write(f"SOFTWARE RULE: {report['software_rule']}\n")
            file.write(f"OBSERVED BEHAVIOR: {report['behavior']}\n")
            file.write(f"ACTUAL RESULT: {report['result']}\n")
            file.write("VALUE CHECK:\n")

            for name, value in report["values"].items():
                file.write(f"  {name}: {value}\n")

            file.write(f"FAILED: {report['failed_values']}\n")
            file.write(f"UNKNOWN: {report['unknown_values']}\n\n")

        print(f"\nREPORT SAVED: {filename}")


def demo_aligned(engine):
    values = {key: True for key in engine.VALUES}

    report = engine.check(
        original_rule="Do not pressure a person.",
        software_rule="The system must not coerce the person.",
        behavior="The person can choose freely and keeps self-respect.",
        result="The person voluntarily performs the good action.",
        values=values,
    )

    engine.print_report(report)


def demo_violation(engine):
    values = {key: True for key in engine.VALUES}
    values["freedom_of_thought"] = False
    values["no_coercion"] = False
    values["self_respect"] = False

    report = engine.check(
        original_rule="Do not pressure a person.",
        software_rule="The system says coercion is not allowed.",
        behavior="The person is threatened with a penalty if they refuse.",
        result="The person acts under pressure.",
        values=values,
    )

    engine.print_report(report)


def demo_review(engine):
    values = {key: True for key in engine.VALUES}
    values["no_coercion"] = None

    report = engine.check(
        original_rule="Do not pressure a person.",
        software_rule="The system has a no-coercion policy.",
        behavior="There is not enough evidence to determine whether pressure occurred.",
        result="The available evidence is incomplete.",
        values=values,
    )

    engine.print_report(report)


def main():
    engine = RBMRuleIntegrity()

    print("=" * 60)
    print("RBM RULE INTEGRITY TESTER")
    print("Version 1.0.0")
    print("=" * 60)

    print("\nTEST 1: ALIGNED")
    demo_aligned(engine)

    print("\nTEST 2: VIOLATION")
    demo_violation(engine)

    print("\nTEST 3: REVIEW")
    demo_review(engine)

    # Save the most important demonstration report.
    engine.save_report(engine.reports[1])


if __name__ == "__main__":
    main()
