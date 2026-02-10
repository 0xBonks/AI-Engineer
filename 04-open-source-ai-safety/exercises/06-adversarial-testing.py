"""
Module 04 - Exercise 06: Adversarial Testing
=============================================

Task: Build a comprehensive adversarial testing framework for AI systems.

Learning Objectives:
- Design adversarial test cases
- Automate security testing
- Document vulnerabilities
- Measure system robustness

Instructions:
-------------
1. Complete the AdversarialTester class
2. Implement attack generation
3. Create vulnerability reports
4. Build defense recommendations

Success Criteria:
-----------------
- Test against 10+ attack vectors
- Generate automated test suites
- Document findings clearly
- Provide actionable recommendations
"""

import os
from typing import List, Dict, Tuple, Callable, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class AttackCategory(Enum):
    """Categories of adversarial attacks."""
    PROMPT_INJECTION = "prompt_injection"
    JAILBREAK = "jailbreak"
    DATA_EXTRACTION = "data_extraction"
    BIAS_EXPLOITATION = "bias_exploitation"
    RESOURCE_EXHAUSTION = "resource_exhaustion"


class VulnerabilityLevel(Enum):
    """Vulnerability severity levels."""
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class AttackVector:
    """An adversarial attack to test."""
    name: str
    category: AttackCategory
    payload: str
    expected_behavior: str
    success_indicators: List[str]


@dataclass
class TestResult:
    """Result of an adversarial test."""
    attack: AttackVector
    response: str
    success: bool
    vulnerability_level: VulnerabilityLevel
    notes: str = ""
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class VulnerabilityReport:
    """Comprehensive vulnerability report."""
    system_name: str
    test_date: datetime
    total_tests: int
    vulnerabilities_found: int
    results_by_category: Dict[AttackCategory, List[TestResult]]
    severity_breakdown: Dict[VulnerabilityLevel, int]
    recommendations: List[str]


class AdversarialTester:
    """Framework for adversarial testing of AI systems."""
    
    def __init__(self, system_name: str = "AI System"):
        """
        Initialize adversarial tester.
        
        Args:
            system_name: Name of system being tested
        """
        self.system_name = system_name
        self.attack_vectors: List[AttackVector] = []
        self.results: List[TestResult] = []
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def add_attack_vector(self, attack: AttackVector) -> None:
        """
        Add an attack vector to test suite.
        
        TODO: Implement this method
        - Append to self.attack_vectors
        - Validate attack has required fields
        """
        # Your code here
        pass
    
    def generate_prompt_injection_attacks(self) -> List[AttackVector]:
        """
        Generate common prompt injection attacks.
        
        Returns:
            List of AttackVector objects
        
        TODO: Implement this method
        - Create attacks for:
            - Instruction override
            - Role switching
            - Context injection
            - Delimiter abuse
            - System prompt extraction
        - Return list of AttackVector objects
        """
        # Your code here
        pass
    
    def generate_jailbreak_attacks(self) -> List[AttackVector]:
        """
        Generate jailbreak attempts.
        
        Returns:
            List of AttackVector objects
        
        TODO: Implement this method
        - Create attacks that try to:
            - Override content policies
            - Pretend restrictions don't apply
            - Use creative scenarios to bypass rules
            - Encode malicious requests
        """
        # Your code here
        pass
    
    def test_system(
        self,
        system_function: Callable[[str], str],
        attack: AttackVector
    ) -> TestResult:
        """
        Test system with an attack vector.
        
        Args:
            system_function: Function that takes input, returns output
            attack: AttackVector to test
        
        Returns:
            TestResult
        
        TODO: Implement this method
        - Call system_function with attack payload
        - Check response against success_indicators
        - Determine if attack succeeded
        - Assess vulnerability level
        - Return TestResult
        """
        # Your code here
        pass
    
    def run_test_suite(
        self,
        system_function: Callable[[str], str],
        attack_vectors: Optional[List[AttackVector]] = None
    ) -> List[TestResult]:
        """
        Run complete test suite against system.
        
        Args:
            system_function: System to test
            attack_vectors: Specific attacks (None = use all)
        
        Returns:
            List of TestResult objects
        
        TODO: Implement this method
        - Use attack_vectors or self.attack_vectors
        - Test each attack
        - Store results
        - Print progress
        - Return results
        """
        # Your code here
        pass
    
    def analyze_response(self, response: str, indicators: List[str]) -> bool:
        """
        Analyze if response indicates successful attack.
        
        Args:
            response: System response
            indicators: Success indicator strings/patterns
        
        Returns:
            True if attack succeeded
        
        TODO: Implement this method
        - Check if any indicator appears in response
        - Use case-insensitive matching
        - Support regex patterns
        - Return True if match found
        """
        # Your code here
        pass
    
    def generate_report(self) -> VulnerabilityReport:
        """
        Generate comprehensive vulnerability report.
        
        Returns:
            VulnerabilityReport
        
        TODO: Implement this method
        - Organize results by category
        - Count vulnerabilities by severity
        - Generate recommendations based on findings
        - Return VulnerabilityReport
        """
        # Your code here
        pass
    
    def print_report(self, report: VulnerabilityReport) -> None:
        """
        Print formatted vulnerability report.
        
        Args:
            report: VulnerabilityReport to print
        
        TODO: Implement this method
        - Format report nicely
        - Use colors/formatting if available
        - Show summary statistics
        - List critical vulnerabilities
        - Display recommendations
        """
        # Your code here
        pass
    
    def export_report(
        self,
        report: VulnerabilityReport,
        filepath: str = "vulnerability_report.txt"
    ) -> None:
        """
        Export report to file.
        
        Args:
            report: VulnerabilityReport
            filepath: Output file path
        
        TODO: Implement this method
        - Format report as markdown or text
        - Include all details
        - Write to file
        - Print confirmation
        """
        # Your code here
        pass


def create_vulnerable_chatbot() -> Callable[[str], str]:
    """
    Create a deliberately vulnerable chatbot for testing.
    
    Returns:
        Function that takes input and returns response
    
    TODO: Implement this function
    - Create simple chatbot with OpenAI
    - NO safety measures (for testing purposes)
    - Return function that accepts string, returns string
    """
    # Your code here
    pass


def create_protected_chatbot() -> Callable[[str], str]:
    """
    Create a protected chatbot for testing.
    
    Returns:
        Function that takes input and returns response
    
    TODO: Implement this function
    - Create chatbot with safety measures
    - Include input validation
    - Include output filtering
    - Return function
    """
    # Your code here
    pass


def test_adversarial_tester():
    """Test the AdversarialTester class."""
    
    tester = AdversarialTester("Test Chatbot")
    
    # Test 1: Generate attacks
    print("Test 1: Generating attacks...")
    injection_attacks = tester.generate_prompt_injection_attacks()
    assert len(injection_attacks) > 0, "Should generate attacks"
    print(f"✓ Generated {len(injection_attacks)} injection attacks")
    
    jailbreak_attacks = tester.generate_jailbreak_attacks()
    assert len(jailbreak_attacks) > 0, "Should generate jailbreaks"
    print(f"✓ Generated {len(jailbreak_attacks)} jailbreak attacks")
    
    # Test 2: Add attack vectors
    print("\nTest 2: Adding attack vectors...")
    for attack in injection_attacks[:3]:
        tester.add_attack_vector(attack)
    assert len(tester.attack_vectors) > 0, "Should store attacks"
    print("✓ Attack vectors added")
    
    # Test 3: Create test system
    print("\nTest 3: Creating test system...")
    vulnerable_bot = create_vulnerable_chatbot()
    assert callable(vulnerable_bot), "Should return function"
    print("✓ Test system created")
    
    # Test 4: Run tests
    print("\nTest 4: Running test suite...")
    results = tester.run_test_suite(vulnerable_bot)
    assert len(results) > 0, "Should return results"
    print(f"✓ Ran {len(results)} tests")
    
    # Test 5: Generate report
    print("\nTest 5: Generating report...")
    report = tester.generate_report()
    assert report is not None, "Should generate report"
    print("✓ Report generated")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # TODO: Complete the implementation and run tests
    # test_adversarial_tester()
    
    # Example usage:
    # tester = AdversarialTester("My Chatbot")
    # 
    # # Load attacks
    # tester.attack_vectors = tester.generate_prompt_injection_attacks()
    # tester.attack_vectors += tester.generate_jailbreak_attacks()
    # 
    # # Test system
    # my_chatbot = create_protected_chatbot()
    # results = tester.run_test_suite(my_chatbot)
    # 
    # # Generate report
    # report = tester.generate_report()
    # tester.print_report(report)
    # tester.export_report(report)
    
    print("TODO: Implement the AdversarialTester class")
    print("Run test_adversarial_tester() when complete")
    print("\n⚠️  Remember: Test responsibly and ethically!")
