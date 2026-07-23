class Policy:
    def __init__(self, policy_id, premium, is_active, coverage_amount):
        self.policy_id = policy_id
        self.premium = premium
        self.is_active = is_active
        self.coverage_amount = coverage_amount  

        """
        Initializes a Policy object.
        """
        """
        Activates the policy.
        """

    def activate_policy(self):
        
        self.is_active = True
        print(f"Policy {self.policy_id} activated: {self.is_active}")


               
    def deactivate_policy(self):  #deactive method
    
        self.is_active = False
        print(f"Policy {self.policy_id} deactivated: {self.is_active}")

    def update_premium(self, premium): # update premium method
        if premium < 0:
            raise ValueError("Premium cannot be negative.")
        self.premium = premium
        print(f"Policy {self.policy_id} updated premium: {self.premium}")

    def increase_coverage(self, amount): # increase coverage method
        if self.coverage_amount + amount < 0:
            raise ValueError("Coverage cannot be negative.")
        self.coverage_amount += amount
        print(f"Policy {self.policy_id} increased coverage: {self.coverage_amount}")

    def decrease_coverage(self, amount): # decrease coverage method
        if self.coverage_amount - amount < 0:
            raise ValueError("Coverage cannot be negative.")
        self.coverage_amount -= amount
        print(f"Policy {self.policy_id} decreased coverage: {self.coverage_amount}")

    def renew_policy(self): # renew policy method
        if not self.is_active:
            raise ValueError("Cannot renew an inactive policy.")
        print(f"Policy {self.policy_id} renewed.")

    def suspend_policy(self): # suspend policy method
        if not self.is_active:
            raise ValueError("Policy is already suspended.")
        self.is_active = False
        print(f"Policy {self.policy_id} suspended.")

    def add_bonus(self, bonus): # add bonus method
        self.premium += bonus
        print(f"Policy {self.policy_id} bonus added: {self.premium}")

    def deduct_penalty(self, penalty): # deduct penalty method
        if self.premium - penalty < 0:
            raise ValueError("Premium cannot be negative.")
        self.premium -= penalty
        print(f"Policy {self.policy_id} penalty deducted: {self.premium}")

    def reset_policy(self): # reset policy method
        self.premium = 0
        self.coverage_amount = 0
        self.is_active = False
        print(f"Policy {self.policy_id} reset to default values.")


class Customer:
    def __init__(self, customer_id, name, email, phone, age, is_premium=False):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.is_premium = is_premium
        self.policy = None
        self.claims = []


class Agent:
    def __init__(self, agent_id, name, email, is_active=True):
        self.agent_id = agent_id
        self.name = name
        self.email = email
        self.is_active = is_active


class Claim:
    def __init__(self, claim_id, amount, status="Pending"):
        self.claim_id = claim_id
        self.amount = amount
        self.status = status


class InsuranceCompany:
    def __init__(self):
        self.policies = []
        self.customers = []
        self.agents = []
        self.claims = []


class Manager:
    def __init__(self, company: InsuranceCompany):
        self.company = company

    # ----- Search helpers -----
    def find_policy(self, policy_id):
        for p in self.company.policies:
            if p.policy_id == policy_id:
                return p
        return None

    def find_customer(self, customer_id):
        for c in self.company.customers:
            if c.customer_id == customer_id:
                return c
        return None

    def find_agent(self, agent_id):
        for a in self.company.agents:
            if a.agent_id == agent_id:
                return a
        return None

    def find_claim(self, claim_id):
        for cl in self.company.claims:
            if cl.claim_id == claim_id:
                return cl
        return None

    # ----- Add / remove -----
    def add_policy(self, policy: Policy):
        if self.find_policy(policy.policy_id):
            raise ValueError("Duplicate policy ID.")
        self.company.policies.append(policy)
        print(f"Policy {policy.policy_id} added.")

    def add_customer(self, customer: Customer):
        if self.find_customer(customer.customer_id):
            raise ValueError("Duplicate customer ID.")
        self.company.customers.append(customer)
        print(f"Customer {customer.customer_id} added.")

    def add_agent(self, agent: Agent):
        if self.find_agent(agent.agent_id):
            raise ValueError("Duplicate agent ID.")
        self.company.agents.append(agent)
        print(f"Agent {agent.agent_id} added.")

    def add_claim(self, claim: Claim):
        if self.find_claim(claim.claim_id):
            raise ValueError("Duplicate claim ID.")
        self.company.claims.append(claim)
        print(f"Claim {claim.claim_id} added.")

    def remove_policy(self, policy: Policy):
        if policy in self.company.policies:
            self.company.policies.remove(policy)
            print(f"Policy {policy.policy_id} removed.")
        else:
            raise ValueError("Policy not found.")

    def remove_customer(self, customer: Customer):
        if customer in self.company.customers:
            self.company.customers.remove(customer)
            print(f"Customer {customer.customer_id} removed.")
        else:
            raise ValueError("Customer not found.")

    def remove_agent(self, agent: Agent):
        if agent in self.company.agents:
            self.company.agents.remove(agent)
            print(f"Agent {agent.agent_id} removed.")
        else:
            raise ValueError("Agent not found.")

    def remove_claim(self, claim: Claim):
        if claim in self.company.claims:
            self.company.claims.remove(claim)
            print(f"Claim {claim.claim_id} removed.")
        else:
            raise ValueError("Claim not found.")

    # ----- Validation -----
    def validate_age(self, age):
        if age < 18:
            raise ValueError("Customer must be at least 18 years old.")
        return True

    def validate_email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        return True

    def validate_phone(self, phone):
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError("Invalid phone number format.")
        return True

    def validate_customer(self, customer: Customer):
        if not customer.name or not customer.email or not customer.phone:
            raise ValueError("Customer must have a name, email, and phone number.")
        self.validate_email(customer.email)
        self.validate_phone(customer.phone)
        self.validate_age(customer.age)
        return True

    def validate_policy(self):
        for p in self.company.policies:
            if p.premium < 0:
                raise ValueError(f"Policy {p.policy_id} has a negative premium.")
            if p.coverage_amount < 0:
                raise ValueError(f"Policy {p.policy_id} has negative coverage.")
        return True

    def validate_claim(self, claim: Claim):
        if claim.amount <= 0:
            raise ValueError("Claim amount must be positive.")
        return True

    # ----- Coordination -----
    def issue_policy(self, policy: Policy, customer: Customer):
        self.validate_customer(customer)
        self.validate_policy()
        self.add_policy(policy)
        customer.policy = policy
        print(f"Policy {policy.policy_id} issued to Customer {customer.customer_id}.")

    def submit_claim(self, claim: Claim, customer: Customer):
        self.validate_customer(customer)
        self.validate_claim(claim)
        self.add_claim(claim)
        customer.claims.append(claim)
        print(f"Claim {claim.claim_id} submitted by Customer {customer.customer_id}.")

    def approve_claim(self, claim: Claim):
        self.validate_claim(claim)
        if claim.status != "Pending":
            raise ValueError("Only pending claims can be approved.")
        claim.status = "Approved"
        print(f"Claim {claim.claim_id} approved.")

    def reject_claim(self, claim: Claim):
        self.validate_claim(claim)
        if claim.status != "Pending":
            raise ValueError("Only pending claims can be rejected.")
        claim.status = "Rejected"
        print(f"Claim {claim.claim_id} rejected.")

    def renew_policy(self, policy: Policy):
        self.validate_policy()
        if not policy.is_active:
            raise ValueError("Cannot renew an inactive policy.")
        policy.is_active = True
        print(f"Policy {policy.policy_id} renewed.")

    def assign_agent(self, customer: Customer, agent: Agent):
        self.validate_customer(customer)
        if not agent.is_active:
            raise ValueError("Cannot assign an inactive agent.")
        customer.agent = agent
        print(f"Agent {agent.agent_id} assigned to Customer {customer.customer_id}.")

    # ----- Display -----
    def display_policy(self, policy: Policy):
        print(f"Policy ID: {policy.policy_id}, Premium: {policy.premium}, "
              f"Active: {policy.is_active}, Coverage: {policy.coverage_amount}")

    def display_customer(self, customer: Customer):
        print(f"Customer ID: {customer.customer_id}, Name: {customer.name}, "
              f"Email: {customer.email}")

    def display_agent(self, agent: Agent):
        print(f"Agent ID: {agent.agent_id}, Name: {agent.name}, Email: {agent.email}")

    def display_claim(self, claim: Claim):
        print(f"Claim ID: {claim.claim_id}, Status: {claim.status}, Amount: {claim.amount}")

    def display_all_policies(self):
        for p in self.company.policies:
            self.display_policy(p)

    def display_all_customers(self):
        for c in self.company.customers:
            self.display_customer(c)

    def display_all_claims(self):
        for cl in self.company.claims:
            self.display_claim(cl)

    def display_company_summary(self):
        print(f"Total Policies: {len(self.company.policies)}")
        print(f"Total Customers: {len(self.company.customers)}")
        print(f"Total Agents: {len(self.company.agents)}")
        print(f"Total Claims: {len(self.company.claims)}")

# Create the insurance company and manager
company = InsuranceCompany()
manager = Manager(company)

# Create customers
c1 = Customer(1, "Alice", "alice@example.com", "9876543210", 25)
c2 = Customer(2, "Bob", "bob@example.com", "9123456780", 30, is_premium=True)

# Create agents
a1 = Agent(101, "Agent X", "agentx@insure.com")
a2 = Agent(102, "Agent Y", "agenty@insure.com", is_active=False)

# Create policies
p1 = Policy(1001, 5000, True, 100000)
p2 = Policy(1002, 7000, True, 200000)

# Create claims
cl1 = Claim(5001, 20000, "Pending")
cl2 = Claim(5002, 5000, "Pending")

# Add to system via manager
manager.add_customer(c1)
manager.add_customer(c2)
manager.add_agent(a1)
manager.add_agent(a2)

manager.issue_policy(p1, c1)
manager.issue_policy(p2, c2)

manager.submit_claim(cl1, c1)
manager.submit_claim(cl2, c2)

# Validate and operate
manager.validate_customer(c1)
manager.assign_agent(c1, a1)

manager.approve_claim(cl1)
manager.reject_claim(cl2)

manager.renew_policy(p1)
p1.add_bonus(500)
p1.decrease_coverage(10000)

# Display
manager.display_all_customers()
manager.display_all_policies()
manager.display_all_claims()
manager.display_company_summary()

