import re

class Policy:
    def __init__(self, policy_id, premium, is_active, coverage_amount):
        self.policy_id = policy_id
        self.premium = premium
        self.is_active = is_active
        self.coverage_amount = coverage_amount


    def activate_policy(self, is_active):
        self.is_active = True
        print(f"policy{self.policy_id} activated:{self.is_active}")

    def deactivate_policy(self, is_active):
        self.is_active = False
        print(f"policy{self.policy} deactivated:{self.is_active}")

    def update_premium(self, premium):
        if premium <0:
            raise ValueError("Premium cannot be negative.")
        self.premium = premium  
        print(f"policy{self.policy_id} updated premium:{self.premium}")

    def increase_coverage(self, amount):
       if self.coverage_amount + amount < 0:
            raise ValueError("Coverage cannot be negative.")
       else:
         self.coverage_amount += amount
         print(f"policy{self.policy_id} increased coverage:{self.coverage_amount}")

    def decrease_coverage(self, amount):
        if self.coverage_amount - amount < 0:
            raise ValueError("Coverage cannot be negative.")
        self.coverage_amount -= amount
        print(f"policy{self.policy_id} decreased coverage:{self.coverage_amount}")

    def renew_policy(self):
        if not self.is_active:
            raise ValueError("Cannot renew an inactive policy.")
        print(f"policy{self.policy_id} renewed.")

    def suspend_policy(self):
        if not self.is_active:
            raise ValueError("Policy is already suspended.")
        self.is_active = False
        print(f"policy{self.policy_id} suspended.")

    def add_bonus(self, bonus):
        self.premium += bonus
        print(f"policy{self.policy_id} bonus added:{self.premium}")

    def deduct_penalty(self, penalty):
        if self.premium - penalty < 0:
            raise ValueError("Premium cannot be negative.")
        self.premium -= penalty
        print(f"policy{self.policy_id} penalty deducted:{self.premium}")    

    def reset_policy(policy):
        policy.premium = 0
        policy.coverage_amount = 0
        policy.is_active = False
        print(f"policy{policy.policy_id} reset to default values.")

"""
Edge Cases
Premium cannot be negative.
Coverage cannot become negative.
Cannot renew an inactive policy.
Level 2 — Search (10 Exercises)"""

class Manager:
    def __init__(self, InsuranceCompany):
        self.InsuranceCompany = InsuranceCompany

    def find_policy(self, policy_id):
        for policy in self.InsuranceCompany.policies:
            if policy.policy_id == policy_id:
                return policy
        return None

    def find_customer(self, customer_id):
        for customer in self.InsuranceCompany.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def find_agent(self, agent_id):
        for agent in self.InsuranceCompany.agents:
            if agent.agent_id == agent_id:
                return agent
        return None

    def find_claim(self, claim_id):
        for claim in self.InsuranceCompany.claims:
            if claim.claim_id == claim_id:
                return claim
        return None

    def find_policy_by_name(self, policy_name):
        for policy in self.InsuranceCompany.policies:
            if policy.policy_name == policy_name:
                return policy
        return None

    def search_active_policy(self):
        return [policy for policy in self.InsuranceCompany.policies if policy.is_active]
    
    def search_customer_phone(self, phone):
        for customer in self.InsuranceCompany.customers:
            if customer.phone == phone:
                return customer
        return None

    def search_customer_email(self, email):
        for customer in self.InsuranceCompany.customers:
            if customer.email == email:
                return customer
        return None

    def search_policy_type(self, policy_type):
        return [policy for policy in self.InsuranceCompany.policies if policy.policy_type == policy_type]

    def search_claim_number(self, claim_number):
        for claim in self.InsuranceCompany.claims:
            if claim.claim_number == claim_number:
                return claim
        return None

    def add_policy(self, policy):
        if self.find_policy(policy.policy_id):
            raise ValueError("Duplicate policy ID.")
        self.InsuranceCompany.policies.append(policy)
        print(f"Policy {policy.policy_id} added.")  

    def add_customer(self, customer):
        if self.find_customer(customer.customer_id):
            raise ValueError("Duplicate customer ID.")
        self.InsuranceCompany.customers.append(customer)
        print(f"Customer {customer.customer_id} added.")        

    def add_agent(self, agent): 
        
        if self.find_agent(agent.agent_id):
            raise ValueError("Duplicate agent ID.")
        self.InsuranceCompany.agents.append(agent)
        print(f"Agent {agent.agent_id} added.")

    def add_claim(self, claim):
        if self.find_claim(claim.claim_id):
            raise ValueError("Duplicate claim ID.")
        self.InsuranceCompany.claims.append(claim)
        print(f"Claim {claim.claim_id} added.")

    def register_customer(self, customer):
        if self.find_customer(customer.customer_id):
            raise ValueError("Duplicate customer ID.")
        self.InsuranceCompany.customers.append(customer)
        print(f"Customer {customer.customer_id} registered.")

    def issue_policy(self, policy):
        if self.find_policy(policy.policy_id):
            raise ValueError("Duplicate policy ID.")
        self.InsuranceCompany.policies.append(policy)
        print(f"Policy {policy.policy_id} issued.")

    def hire_agent(self, agent):
        if self.find_agent(agent.agent_id):
            raise ValueError("Duplicate agent ID.")
        self.InsuranceCompany.agents.append(agent)
        print(f"Agent {agent.agent_id} hired.")

    def add_family_member(self, family_member):
        if self.find_customer(family_member.customer_id):
            raise ValueError("Duplicate family member ID.")
        self.InsuranceCompany.customers.append(family_member)
        print(f"Family member {family_member.customer_id} added.")

    def add_vehicle_policy(self, policy):
        if self.find_policy(policy.policy_id):
            raise ValueError("Duplicate policy ID.")
        self.InsuranceCompany.policies.append(policy)
        print(f"Vehicle policy {policy.policy_id} added.")

    def add_health_policy(self, policy):
        if self.find_policy(policy.policy_id):
            raise ValueError("Duplicate policy ID.")
        self.InsuranceCompany.policies.append(policy)
        print(f"Health policy {policy.policy_id} added.") 

    def remove_policy(self, policy):
        if policy in self.InsuranceCompany.policies:
            self.InsuranceCompany.policies.remove(policy)
            print(f"Policy {policy.policy_id} removed.")
        else:
            raise ValueError("Policy not found.")
        
    def remove_customer(self, customer):
        if customer in self.InsuranceCompany.customers:
            self.InsuranceCompany.customers.remove(customer)
            print(f"Customer {customer.customer_id} removed.")
        else:
            raise ValueError("Customer not found.")
        
    def remove_agent(self, agent):
        if agent in self.InsuranceCompany.agents:
            self.InsuranceCompany.agents.remove(agent)
            print(f"Agent {agent.agent_id} removed.")
        else:
            raise ValueError("Agent not found.")
        
    def remove_claim(self, claim):
        if claim in self.InsuranceCompany.claims:
            self.InsuranceCompany.claims.remove(claim)
            print(f"Claim {claim.claim_id} removed.")
        else:
            raise ValueError("Claim not found.")
        
    def cancel_policy(self, policy):
        if policy in self.InsuranceCompany.policies:
            self.InsuranceCompany.policies.remove(policy)
            print(f"Policy {policy.policy_id} canceled.")
        else:
            raise ValueError("Policy not found.")

        
    def terminate_agent(self, agent):
        if agent in self.InsuranceCompany.agents:
            self.InsuranceCompany.agents.remove(agent)
            print(f"Agent {agent.agent_id} terminated.")
        else:
            raise ValueError("Agent not found.")


    def delete_customer(self, customer):
        if customer in self.InsuranceCompany.customers:
            self.InsuranceCompany.customers.remove(customer)
            print(f"Customer {customer.customer_id} deleted.")
        else:
            raise ValueError("Customer not found.")
        
    def remove_family_member(self, family_member):
        if family_member in self.InsuranceCompany.customers:
            self.InsuranceCompany.customers.remove(family_member)
            print(f"Family member {family_member.customer_id} removed.")
        else:
            raise ValueError("Family member not found.")
        
    def remove_vehicle(self, vehicle):
        if vehicle in self.InsuranceCompany.vehicles:
            self.InsuranceCompany.vehicles.remove(vehicle)
            print(f"Vehicle {vehicle.vehicle_id} removed.")
        else:
            raise ValueError("Vehicle not found.")
        
    def delete_expired_policy(self, policy):
        if policy in self.InsuranceCompany.policies:
            self.InsuranceCompany.policies.remove(policy)
            print(f"Expired policy {policy.policy_id} deleted.")
        else:
            raise ValueError("Policy not found.")
        

    def active_policies(self, is_active=True):
        return [policy for policy in self.InsuranceCompany.policies if policy.is_active == is_active]

    def expired_policies(self):
        return [policy for policy in self.InsuranceCompany.policies if not policy.is_active]    

    def pending_claims(self):
        return [claim for claim in self.InsuranceCompany.claims if claim.status == "Pending"]

    def approved_claims(self):
        return [claim for claim in self.InsuranceCompany.claims if claim.status == "Approved"]

    def rejected_claims(self):
        return [claim for claim in self.InsuranceCompany.claims if claim.status == "Rejected"]

    def high_value_policies(self):
        return [policy for policy in self.InsuranceCompany.policies if policy.value > 10000]

    def premium_customers(self):
        return [customer for customer in self.InsuranceCompany.customers if customer.is_premium]

    def active_agents(self):
        return [agent for agent in self.InsuranceCompany.agents if agent.is_active]

    def unpaid_policies(self):
        return [policy for policy in self.InsuranceCompany.policies if not policy.is_paid]

    def low_coverage_policies(self):
        return [policy for policy in self.InsuranceCompany.policies if policy.coverage < 0.5]
# dispay methods

    def display_policy(self, policy):
        print(f"Policy ID: {policy.policy_id}, Premium: {policy.premium}, Active: {policy.is_active}, Coverage: {policy.coverage_amount}")
        
    def display_customer(self, customer):
        print(f"Customer ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}")

    def display_agent(self, agent):
        print(f"Agent ID: {agent.agent_id}, Name: {agent.name}, Email: {agent.email}")

    def display_claim(self, claim):
        print(f"Claim ID: {claim.claim_id}, Status: {claim.status}, Amount: {claim.amount}")
        
    def display_all_policies(self):
        for policy in self.InsuranceCompany.policies:
            self.display_policy(policy)

    def display_all_customers(self):
        for customer in self.InsuranceCompany.customers:
            self.display_customer(customer)

    def display_pending_claims(self):
        for claim in self.pending_claims():
            self.display_claim(claim)

    def display_expired_policies(self):
        for policy in self.expired_policies():
            self.display_policy(policy) 

    def display_agent_clients(self):    
        for agent in self.InsuranceCompany.agents:
            print(f"Agent ID: {agent.agent_id}, Name: {agent.name}")
            for customer in self.InsuranceCompany.customers:
                if customer.agent_id == agent.agent_id:
                    self.display_customer(customer)

    def display_company_summary(self):
        print(f"Total Policies: {len(self.InsuranceCompany.policies)}")
        print(f"Total Customers: {len(self.InsuranceCompany.customers)}")
        print(f"Total Agents: {len(self.InsuranceCompany.agents)}")
        print(f"Total Claims: {len(self.InsuranceCompany.claims)}")

#Level 7 — Validation 

    def validate_age(self, age):
        if age < 18:
            raise ValueError("Customer must be at least 18 years old.")
        return True
    
    def validate_policy(self):
        for policy in self.InsuranceCompany.policies:
            if policy.premium < 0:
                raise ValueError(f"Policy {policy.policy_id} has a negative premium.")
            if policy.coverage_amount < 0:
                raise ValueError(f"Policy {policy.policy_id} has negative coverage.")
        return True
    
    
    def validate_email(email):
       pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
       if not re.match(pattern, email):
        raise ValueError("Invalid email format.")
        return True
       
    def validate_phone(self, phone):
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError("Invalid phone number format.")
        return True

    def validate_claim(self, claim):
        if claim.amount <= 0:
            raise ValueError("Claim amount must be positive.")
        return True

    def validate_premium(self, premium):
        if premium < 0:
            raise ValueError("Premium must be a positive value.")
        return True

    def validate_coverage(self, coverage):
        if coverage < 0 or coverage > 1:
            raise ValueError("Coverage must be a value between 0 and 1.")
        return True
    
    def validate_policy_status(self):
        for policy in self.InsuranceCompany.policies:
            if not isinstance(policy.is_active, bool):
                raise ValueError(f"Policy {policy.policy_id} has an invalid status.")
        return True
    
    def validate_customer(self, customer):
        if not customer.name or not customer.email or not customer.phone:
            raise ValueError("Customer must have a name, email, and phone number.")
        self.validate_email(customer.email)
        self.validate_phone(customer.phone)
        return True
    

#Level 8 — Coordination (10 Exercises)
    def issue_policy(self, policy, customer):
        self.validate_customer(customer)
        self.validate_policy()
        self.InsuranceCompany.policies.append(policy)
        customer.policy = policy
        print(f"Policy {policy.policy_id} issued to Customer {customer.customer_id}.")

    def submit_claim(self, claim, customer):
        self.validate_customer(customer)
        self.validate_claim(claim)
        self.InsuranceCompany.claims.append(claim)
        customer.claims.append(claim)
        print(f"Claim {claim.claim_id} submitted by Customer {customer.customer_id}.")
        
    def approve_claim(self, claim):
        self.validate_claim(claim)
        claim.status = "Approved"
        print(f"Claim {claim.claim_id} approved.")

    def reject_claim(self, claim):
        self.validate_claim(claim)
        claim.status = "Rejected"
        print(f"Claim {claim.claim_id} rejected.")

    def renew_policy(self, policy):
        self.validate_policy()
        if not policy.is_active:
            raise ValueError("Cannot renew an inactive policy.")
        policy.is_active = True
        print(f"Policy {policy.policy_id} renewed.")

    def assign_agent(self, customer, agent):
        self.validate_customer(customer)
        if not agent.is_active:
            raise ValueError("Cannot assign an inactive agent.")
        customer.agent = agent
        print(f"Agent {agent.agent_id} assigned to Customer {customer.customer_id}.")

    def transfer_customer(self, customer, new_agent):   
        self.validate_customer(customer)
        if not new_agent.is_active:
            raise ValueError("Cannot transfer to an inactive agent.")
        customer.agent = new_agent
        print(f"Customer {customer.customer_id} transferred to Agent {new_agent.agent_id}.")

    def cancel_policy(self, policy):
        self.validate_policy()
        if policy in self.InsuranceCompany.policies:
            self.InsuranceCompany.policies.remove(policy)
            print(f"Policy {policy.policy_id} canceled.")
        else:
            raise ValueError("Policy not found.")
        
    def process_payment(self, payment):
        if payment.amount <= 0:
            raise ValueError("Payment amount must be positive.")
        payment.status = "Processed"
        print(f"Payment of {payment.amount} processed.")

    def pay_claim(self, claim):
        self.validate_claim(claim)
        if claim.status != "Approved":
            raise ValueError("Cannot pay a claim that is not approved.")
        claim.status = "Paid"
        print(f"Claim {claim.claim_id} paid.")


#Level 9 — Inheritance & Polymorphism (10 Exercises)

class Person:
    def __init__(self, Customer, Agent):
        self.Customer = Customer
        self.Agent = Agent

class Policy:
    def __init__(self, HealthPolicy, VehiclePolicy, LifePolicy):
        self.HealthPolicy = HealthPolicy
        self.VehiclePolicy = VehiclePolicy
        self.LifePolicy = LifePolicy


#9.1.Override:
    def calculate_premium(self, HealthPolicy, VehiclePolicy, LifePolicy):
        if isinstance(self, HealthPolicy):
            return self.base_premium * 1.2
        elif isinstance(self, VehiclePolicy):
            return self.base_premium * 1.5
        elif isinstance(self, LifePolicy):
            return self.base_premium * 1.8
        else:
            return self.base_premium
        
    def display(self):
      print(f"Policy ID: {self.policy_id}, Premium: {self.premium}, Active: {self.is_active}, Coverage: {self.coverage_amount}")

    def calculate_bonus(self):
        if self.is_active:
            return self.premium * 0.1
        else:
            return 0    
        
    def approve_claim(self):
        if self.status == "Pending":
            self.status = "Approved"
            print(f"Claim {self.claim_id} approved.")
        else:
            raise ValueError("Claim is not pending.")
        
    def calculate_tax(self, amount):
        tax_rate = 0.05
        return amount * tax_rate

    def calculate_discount(self):
        if self.is_active:
            return self.premium * 0.05
        else:
            return 0
        
    def process_payment(self, payment):
        if payment.amount <= 0:
            raise ValueError("Payment amount must be positive.")
        payment.status = "Processed"
        print(f"Payment of {payment.amount} processed.")

    def show_policy(self):
        print(f"Policy ID: {self.policy_id}, Premium: {self.premium}, Active: {self.is_active}, Coverage: {self.coverage_amount}") 

    def show_details(self):
        print(f"Policy ID: {self.policy_id}, Premium: {self.premium}, Active: {self.is_active}, Coverage: {self.coverage_amount}")

    def policy_summary(self):
        print(f"Policy ID: {self.policy_id}, Premium: {self.premium}, Active: {self.is_active}, Coverage: {self.coverage_amount}")  

