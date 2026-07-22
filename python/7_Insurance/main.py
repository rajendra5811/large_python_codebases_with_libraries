class Policy:
    def __init__(self, policy_id, premium, is_active, coverage_amount):
        self.policy_id = policy_id
        self.premium = premium
        self.is_active = is_active
        self.coverage_amount = coverage_amount

    def activate_policy(self, is_active):
        self.is_active = is_active
        print(f"Policy {self.policy_id} activated: {self.is_active}")

    def deactivate_policy(self):
        self.is_active = False
        print(f"Policy {self.policy_id} deactivated: {self.is_active}")

    def update_premium(self, new_premium):
        if new_premium < 0:
            print("Error: Premium cannot be negative.")
            return
        self.premium = new_premium
        print(f"Policy {self.policy_id} premium updated: {self.premium}")

    def increase_coverage(self, amount):
        if self.coverage_amount + amount < 0:
            print("Error: Coverage cannot become negative.")
            return
        self.coverage_amount += amount
        print(f"Policy {self.policy_id} coverage increased: {self.coverage_amount}")

    def decrease_coverage(self, amount):
        if self.coverage_amount - amount < 0:
            print("Error: Coverage cannot become negative.")
            return
        self.coverage_amount -= amount
        print(f"Policy {self.policy_id} coverage decreased: {self.coverage_amount}")

    def renew_policy(self):
        if not self.is_active:
            print("Error: Cannot renew an inactive policy.")
            return
        print(f"Policy {self.policy_id} renewed.")

    def suspend_policy(self):
        self.is_active = False
        print(f"Policy {self.policy_id} suspended.")

    def add_bonus(self, amount):
        self.premium += amount
        print(f"Policy {self.policy_id} bonus added: {self.premium}")

    def deduct_penalty(self, amount):
        self.premium -= amount
        print(f"Policy {self.policy_id} penalty deducted: {self.premium}")

    def reset_policy(self):
        self.premium = 0
        self.coverage_amount = 0
        print(f"Policy {self.policy_id} reset.")
deduct_penalty()
reset_policy()

Edge Cases
Premium cannot be negative.
Coverage cannot become negative.
Cannot renew an inactive policy.