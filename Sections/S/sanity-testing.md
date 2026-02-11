# Sanity Testing
[Sanity Testing](#sanity-testing)[Sanity testing](/wiki/sanity-testing)[regression testing](/wiki/regression-testing)
### Related Terms:
- Build Verification Testing
[Build Verification Testing](/glossary/build-verification-testing)
## Questions aboutSanity Testing?

#### Basics and Importance
- What is sanity testing in software testing?Sanity testingis a subset ofregression testingfocused on verifying specific functionality after minor changes orbugfixes. It's a quick, non-exhaustive check to ensure that a particular function orbugis working as expected post-modification. Unlike smoke testing, which is broad and shallow,sanity testingis narrow and deep, concentrating on one or a few areas of functionality.When determining functionalities to test, prioritize those directly affected by recent code changes.Sanity testingis typically brief, often completed in a matter of hours, and is crucial for maintaining quality in fast-paced development environments like Agile.In continuous integration, sanity tests are triggered after a successful build and smoke test. They serve as a gatekeeper, ensuring that new changes do not disrupt key features before more rigorous testing is performed.Common techniques include targetedretestingand usingexploratory testingto focus on affected functionalities. While sanity tests can be reused, they often require updates to align with the latest application changes.Automation plays a significant role insanity testing, enabling rapid execution of these focused tests. Automated sanity tests are scripted, maintained in version control, and integrated into the CI/CD pipeline.Results should be documented clearly and concisely, often intest managementtools or integrated into the CI/CD reporting mechanisms.Best practices include maintaining a leantest suite, focusing on critical functionalities, and ensuring tests are easy to update. Tools likeSelenium, TestComplete, or specific CI tools like Jenkins or CircleCI are commonly used to facilitatesanity testing.
- Why is sanity testing important in the software development lifecycle?Sanity testingis crucial in the software development lifecycle as it ensures that recent changes orbugfixes have not adversely affected existing functionalities. It acts as aquick health checkpost a minor code change, verifying that a particular function orbugis working as expected. This targeted testing approach saves time and resources by notretestingthe entire application, focusing only on the affected areas and their related functionalities.By confirming that the core aspects of a release are functioning correctly,sanity testinghelps maintain a stable build and prevents the propagation of glaring issues into later stages of development. It's particularly important when there arefrequent releases or continuous deployments, as it allows for rapid validation of critical functionality without the overhead of a full regression suite.In anAgile environment, sanity tests are often automated to provide immediate feedback on the stability of the application after eachiteration. They serve as a gatekeeper, ensuring that the most recent changes are sound before moving on to more extensive testing phases or before a build is promoted to the next environment.Sanity testing's importance is underscored by its role in maintaining a high level of confidence in the software's reliability, especially when time constraints or resource limitations make fullregression testingimpractical. It helps teams prioritize issues, streamline the development process, and deliver quality software at a faster pace.
- How does sanity testing differ from smoke testing?Sanity testingand smoke testing are both subsets ofacceptance testing, yet they serve different purposes and occur at different stages of the software release cycle.Smoke testingis a preliminary test that checks the basic functionality of an application after a new build to ensure that the major features are working and that the build is stable enough for further testing. It's like an initial health check of the software.In contrast,sanity testingis a more focused form of testing that is performed after receiving a software build with minor changes or in a stable development phase. It ensures that the specific issue or functionality that was updated works as expected without performing exhaustive testing.Sanity testingis usually unscripted and helps in verifying the rationality of the system, ensuring that the proposed functionality works roughly as intended.While smoke testing is broad and shallow,sanity testingis narrow and deep. Smoke testing is often automated, acting as a gatekeeper for further testing, whereassanity testingcan be either manual or automated and is used to check specific components after changes have been made.In essence, smoke testing asks "Does the application broadly function?" whilesanity testingasks "Do the recent changes make sense and function correctly?" Both are critical in the software development lifecycle but are applied at different points and for different reasons.
- What are the key benefits of performing sanity testing?Sanity testingoffers several key benefits:Quick Feedback: It provides immediate validation of core functionalities after minor changes, ensuring that any defects are identified quickly.Cost-Effective: By focusing on specific areas, it saves time and resources compared to a full regression test.Focus on Critical Issues: Sanity testing zeroes in on critical functionalities, which can be crucial for decision-making processes regarding further testing or releases.Simplifies Testing: It simplifies the assessment of a particular segment of the application, making it easier to perform and understand.Enhances Quality: Regular sanity checks help maintain a high quality of the product by catching issues in the early stages of development.Supports Continuous Integration: In a CI environment, sanity tests can be run automatically to verify that new code commits have not disrupted key features.Sanity testingis a strategic approach to verify that a particular function orbugfix works as intended. It's a subset ofregression testingand is often used as a checkpoint to determine if the application is ready for further, more extensive testing. By incorporating sanity tests into thetest suite, teams can ensure that the most crucial aspects of the software are always in working order, which is especially beneficial in fast-paced development environments where frequent changes are made.
- What is the role of sanity testing in Agile methodology?In Agile methodology,sanity testingserves as a focused check to ensure that a specific function orbugfix works as intended after a minor change or in a new build. It's a quick, narrow regression test to validate that the code changes have not disrupted existing functionality.Sanity testingis typically done aftersmoke testingand before more extensiveregression testingoruser acceptance testing(UAT).Agile teams often employ sanity tests during continuous integration and deployment (CI/CD) to verify that recent commits haven't introduced any major issues. This is crucial in Agile's iterative development cycle, where changes are frequent and rapid.Since Agile emphasizesuser satisfactionandworking software,sanity testingaligns with these principles by quickly confirming that the most recent changes haven't compromised the user experience or core functionality. It helps maintain a stable product for the nextiterationof development.Sanity tests are usuallymanualbut can be automated for efficiency. They are often derived from a subset of regression tests that are most relevant to the recent changes. While they can be reused, they should be regularly reviewed and updated to align with the evolving software.Documentationfor sanity tests should be concise, capturing the essence of what was tested and the outcome. This documentation aids in communication within the team and serves as a reference for future testing cycles.Best practicesinclude prioritizing tests based on the impact of changes, keeping sanity tests lean, and ensuring they are easily maintainable and adaptable to changes in the software.

Sanity testingis a subset ofregression testingfocused on verifying specific functionality after minor changes orbugfixes. It's a quick, non-exhaustive check to ensure that a particular function orbugis working as expected post-modification. Unlike smoke testing, which is broad and shallow,sanity testingis narrow and deep, concentrating on one or a few areas of functionality.
[Sanity testing](/wiki/sanity-testing)[regression testing](/wiki/regression-testing)[bug](/wiki/bug)[bug](/wiki/bug)[sanity testing](/wiki/sanity-testing)
When determining functionalities to test, prioritize those directly affected by recent code changes.Sanity testingis typically brief, often completed in a matter of hours, and is crucial for maintaining quality in fast-paced development environments like Agile.
[Sanity testing](/wiki/sanity-testing)
In continuous integration, sanity tests are triggered after a successful build and smoke test. They serve as a gatekeeper, ensuring that new changes do not disrupt key features before more rigorous testing is performed.

Common techniques include targetedretestingand usingexploratory testingto focus on affected functionalities. While sanity tests can be reused, they often require updates to align with the latest application changes.
[retesting](/wiki/retesting)[exploratory testing](/wiki/exploratory-testing)
Automation plays a significant role insanity testing, enabling rapid execution of these focused tests. Automated sanity tests are scripted, maintained in version control, and integrated into the CI/CD pipeline.
[sanity testing](/wiki/sanity-testing)
Results should be documented clearly and concisely, often intest managementtools or integrated into the CI/CD reporting mechanisms.
[test management](/wiki/test-management)
Best practices include maintaining a leantest suite, focusing on critical functionalities, and ensuring tests are easy to update. Tools likeSelenium, TestComplete, or specific CI tools like Jenkins or CircleCI are commonly used to facilitatesanity testing.
[test suite](/wiki/test-suite)[Selenium](/wiki/selenium)[sanity testing](/wiki/sanity-testing)
Sanity testingis crucial in the software development lifecycle as it ensures that recent changes orbugfixes have not adversely affected existing functionalities. It acts as aquick health checkpost a minor code change, verifying that a particular function orbugis working as expected. This targeted testing approach saves time and resources by notretestingthe entire application, focusing only on the affected areas and their related functionalities.
[Sanity testing](/wiki/sanity-testing)[bug](/wiki/bug)**quick health check**[bug](/wiki/bug)[retesting](/wiki/retesting)
By confirming that the core aspects of a release are functioning correctly,sanity testinghelps maintain a stable build and prevents the propagation of glaring issues into later stages of development. It's particularly important when there arefrequent releases or continuous deployments, as it allows for rapid validation of critical functionality without the overhead of a full regression suite.
[sanity testing](/wiki/sanity-testing)**frequent releases or continuous deployments**
In anAgile environment, sanity tests are often automated to provide immediate feedback on the stability of the application after eachiteration. They serve as a gatekeeper, ensuring that the most recent changes are sound before moving on to more extensive testing phases or before a build is promoted to the next environment.
**Agile environment**[iteration](/wiki/iteration)
Sanity testing's importance is underscored by its role in maintaining a high level of confidence in the software's reliability, especially when time constraints or resource limitations make fullregression testingimpractical. It helps teams prioritize issues, streamline the development process, and deliver quality software at a faster pace.
[Sanity testing](/wiki/sanity-testing)[regression testing](/wiki/regression-testing)
Sanity testingand smoke testing are both subsets ofacceptance testing, yet they serve different purposes and occur at different stages of the software release cycle.Smoke testingis a preliminary test that checks the basic functionality of an application after a new build to ensure that the major features are working and that the build is stable enough for further testing. It's like an initial health check of the software.
[Sanity testing](/wiki/sanity-testing)[acceptance testing](/wiki/acceptance-testing)**Smoke testing**
In contrast,sanity testingis a more focused form of testing that is performed after receiving a software build with minor changes or in a stable development phase. It ensures that the specific issue or functionality that was updated works as expected without performing exhaustive testing.Sanity testingis usually unscripted and helps in verifying the rationality of the system, ensuring that the proposed functionality works roughly as intended.
**sanity testing**[sanity testing](/wiki/sanity-testing)[Sanity testing](/wiki/sanity-testing)
While smoke testing is broad and shallow,sanity testingis narrow and deep. Smoke testing is often automated, acting as a gatekeeper for further testing, whereassanity testingcan be either manual or automated and is used to check specific components after changes have been made.
[sanity testing](/wiki/sanity-testing)[sanity testing](/wiki/sanity-testing)
In essence, smoke testing asks "Does the application broadly function?" whilesanity testingasks "Do the recent changes make sense and function correctly?" Both are critical in the software development lifecycle but are applied at different points and for different reasons.
[sanity testing](/wiki/sanity-testing)
Sanity testingoffers several key benefits:
[Sanity testing](/wiki/sanity-testing)- Quick Feedback: It provides immediate validation of core functionalities after minor changes, ensuring that any defects are identified quickly.
- Cost-Effective: By focusing on specific areas, it saves time and resources compared to a full regression test.
- Focus on Critical Issues: Sanity testing zeroes in on critical functionalities, which can be crucial for decision-making processes regarding further testing or releases.
- Simplifies Testing: It simplifies the assessment of a particular segment of the application, making it easier to perform and understand.
- Enhances Quality: Regular sanity checks help maintain a high quality of the product by catching issues in the early stages of development.
- Supports Continuous Integration: In a CI environment, sanity tests can be run automatically to verify that new code commits have not disrupted key features.
**Quick Feedback****Cost-Effective****Focus on Critical Issues****Simplifies Testing****Enhances Quality****Supports Continuous Integration**
Sanity testingis a strategic approach to verify that a particular function orbugfix works as intended. It's a subset ofregression testingand is often used as a checkpoint to determine if the application is ready for further, more extensive testing. By incorporating sanity tests into thetest suite, teams can ensure that the most crucial aspects of the software are always in working order, which is especially beneficial in fast-paced development environments where frequent changes are made.
[Sanity testing](/wiki/sanity-testing)[bug](/wiki/bug)[regression testing](/wiki/regression-testing)[test suite](/wiki/test-suite)
In Agile methodology,sanity testingserves as a focused check to ensure that a specific function orbugfix works as intended after a minor change or in a new build. It's a quick, narrow regression test to validate that the code changes have not disrupted existing functionality.Sanity testingis typically done aftersmoke testingand before more extensiveregression testingoruser acceptance testing(UAT).
**sanity testing**[sanity testing](/wiki/sanity-testing)[bug](/wiki/bug)[Sanity testing](/wiki/sanity-testing)**smoke testing**[regression testing](/wiki/regression-testing)[user acceptance testing](/wiki/user-acceptance-testing)
Agile teams often employ sanity tests during continuous integration and deployment (CI/CD) to verify that recent commits haven't introduced any major issues. This is crucial in Agile's iterative development cycle, where changes are frequent and rapid.

Since Agile emphasizesuser satisfactionandworking software,sanity testingaligns with these principles by quickly confirming that the most recent changes haven't compromised the user experience or core functionality. It helps maintain a stable product for the nextiterationof development.
**user satisfaction****working software**[sanity testing](/wiki/sanity-testing)[iteration](/wiki/iteration)
Sanity tests are usuallymanualbut can be automated for efficiency. They are often derived from a subset of regression tests that are most relevant to the recent changes. While they can be reused, they should be regularly reviewed and updated to align with the evolving software.
**manual**
Documentationfor sanity tests should be concise, capturing the essence of what was tested and the outcome. This documentation aids in communication within the team and serves as a reference for future testing cycles.
**Documentation**
Best practicesinclude prioritizing tests based on the impact of changes, keeping sanity tests lean, and ensuring they are easily maintainable and adaptable to changes in the software.
**Best practices**
#### Process and Techniques
- What are the steps involved in the sanity testing process?Sanity testinginvolves a subset of tests focused on validating specific functionality after minor changes. Here's a concise rundown of the steps:Identify Changed Features: Pinpoint the features impacted by recent code changes.SelectTest Cases: Choose relevant test cases that cover the affected functionalities.Set UpTest Environment: Prepare the environment to reflect the production setup.Execute Tests: Run the selected test cases manually or through automated scripts.Analyze Results: Evaluate test outcomes to ensure the changes work as expected.Report Findings: Document any defects or issues and communicate them to the development team.Retest: After fixes, retest to confirm issues are resolved.Remember, sanity tests are quick, targeted, and not exhaustive. They ensure that a particular function orbugfix works without unintended side effects.
- What techniques are commonly used in sanity testing?Sanity testingcommonly employs a focused and narrow set of techniques to verify that a particular function orbugfix works as expected after a minor code change. Here are some techniques used:SelectiveTest CaseExecution: Running a subset of test cases that are directly related to the recent code changes.Priority-based Testing: Executing tests for critical functionalities first to ensure they are not affected by recent changes.Exploratory Testing: Informal testing where the tester actively controls the design of the tests as they are performed.Retest All: In some cases, sanity testing may involve re-running all existing test cases for the modified component to ensure no new issues have been introduced.Test CaseSampling: Choosing a few test cases that represent the larger set of tests to quickly verify the system's health.Incorporating automation intosanity testinginvolves scripting these techniques to be executed automatically:// Example of an automated sanity test script
describe('Sanity Test Suite', () => {
  it('should verify critical functionality A works', () => {
    // Test steps for functionality A
  });

  it('should verify critical functionality B works', () => {
    // Test steps for functionality B
  });

  // Additional test cases...
});Automated sanity tests are typically integrated into the CI/CD pipeline to run after each build deployment. Results are documented intest reportsgenerated by the automation framework or CI tool, which are then reviewed to make decisions about the stability of the build.
- How do you determine which functionalities to test in sanity testing?Determining which functionalities to test insanity testinginvolves focusing on the most critical aspects of the software that have been recently modified or impacted by code changes. To select these functionalities, consider the following criteria:RecentBugFixes: Prioritize functionalities that have undergone recent bug fixes to ensure the fixes are effective and have not introduced new issues.New Features: Test new features that are critical for the application's operation and are likely to be used frequently by end-users.High-Risk Areas: Identify areas of the application that are prone to errors or have a history of issues, as these are more likely to break with new changes.Core Functionalities: Focus on the core functionalities that are essential for the application to run smoothly, as any issues here can render the software unusable.Dependencies: Consider functionalities that have dependencies on the modified code, as changes can have cascading effects on related features.Use a risk-based approach to prioritize testing efforts, ensuring that the most impactful and critical areas are covered. Collaborate with developers, product managers, and other stakeholders to understand the scope of changes and their potential impact on the application. This collaboration helps in creating a targeted sanitytest suitethat is both efficient and effective.
- What is the typical duration of a sanity test?The typical duration of asanity testvaries depending on the scope of the changes made to the software and the size of the project. Generally, sanity tests are brief, often taking anywhere from15 minutes to a few hoursto execute. These tests are designed to be quick checks to ensure that the most crucial functions work as expected after minor modifications.Sincesanity testingis a subset ofregression testing, it focuses on specific areas rather than the entire application. The duration is kept short to facilitate rapid feedback to the development team. In acontinuous integrationenvironment, sanity tests may run even faster, as they are automated and executed as soon as a new build is available.For experiencedtest automationengineers, it's essential to have a well-optimized suite of sanity tests that can be triggered automatically. This suite should be concise yet comprehensive enough to cover the critical functionalities that could be affected by recent code changes. The speed of execution can be further enhanced by parallel execution and efficienttest managementpractices.Remember, the goal ofsanity testingis to quickly determine whether it's reasonable to proceed with further, more exhaustive testing. Therefore, the duration should align with this objective, ensuring a balance between thoroughness and time efficiency.
- How is sanity testing performed in a continuous integration environment?In acontinuous integration (CI)environment,sanity testingis typically automated and integrated into the CI pipeline. The process is as follows:Code Commit: Developers push code to the repository, triggering the CI pipeline.Build: The CI server compiles the code into an executable application.Deploy: The build is deployed to a test environment automatically.SanityTest Suite: A predefined suite of sanity tests is executed. These tests are a subset of the regression suite, focusing on critical functionalities.Test Execution: Automated scripts run the sanity tests. These scripts are often written in a high-level language and managed by a test framework.Results Analysis: Test results are automatically collected and analyzed. Failures halt the pipeline, and stakeholders are notified.Feedback Loop: Developers receive immediate feedback on the build's sanity, allowing for quick fixes if necessary.// Example of a sanity test script in TypeScript
import { expect } from 'chai';
import { login, getUserProfile } from './appActions';

describe('Sanity Test Suite', () => {
  it('should successfully log in and retrieve user profile', async () => {
    const loginResponse = await login('user', 'password');
    expect(loginResponse).to.be.true;

    const profile = await getUserProfile();
    expect(profile).to.have.property('username');
  });
});Automated sanity tests are designed to befastandfocused, providing a quick check to ensure that the most crucial parts of the application are functioning after each build. Results are typically logged into atest managementtool or directly into the CI system for easy access and review.

Sanity testinginvolves a subset of tests focused on validating specific functionality after minor changes. Here's a concise rundown of the steps:
[Sanity testing](/wiki/sanity-testing)1. Identify Changed Features: Pinpoint the features impacted by recent code changes.
2. SelectTest Cases: Choose relevant test cases that cover the affected functionalities.
3. Set UpTest Environment: Prepare the environment to reflect the production setup.
4. Execute Tests: Run the selected test cases manually or through automated scripts.
5. Analyze Results: Evaluate test outcomes to ensure the changes work as expected.
6. Report Findings: Document any defects or issues and communicate them to the development team.
7. Retest: After fixes, retest to confirm issues are resolved.
**Identify Changed Features****SelectTest Cases**[Test Cases](/wiki/test-case)**Set UpTest Environment**[Test Environment](/wiki/test-environment)**Execute Tests****Analyze Results****Report Findings****Retest**
Remember, sanity tests are quick, targeted, and not exhaustive. They ensure that a particular function orbugfix works without unintended side effects.
[bug](/wiki/bug)
Sanity testingcommonly employs a focused and narrow set of techniques to verify that a particular function orbugfix works as expected after a minor code change. Here are some techniques used:
[Sanity testing](/wiki/sanity-testing)[bug](/wiki/bug)- SelectiveTest CaseExecution: Running a subset of test cases that are directly related to the recent code changes.
- Priority-based Testing: Executing tests for critical functionalities first to ensure they are not affected by recent changes.
- Exploratory Testing: Informal testing where the tester actively controls the design of the tests as they are performed.
- Retest All: In some cases, sanity testing may involve re-running all existing test cases for the modified component to ensure no new issues have been introduced.
- Test CaseSampling: Choosing a few test cases that represent the larger set of tests to quickly verify the system's health.
**SelectiveTest CaseExecution**[Test Case](/wiki/test-case)**Priority-based Testing**[Priority](/wiki/priority)**Exploratory Testing**[Exploratory Testing](/wiki/exploratory-testing)**Retest All****Test CaseSampling**[Test Case](/wiki/test-case)
Incorporating automation intosanity testinginvolves scripting these techniques to be executed automatically:
[sanity testing](/wiki/sanity-testing)
```
// Example of an automated sanity test script
describe('Sanity Test Suite', () => {
  it('should verify critical functionality A works', () => {
    // Test steps for functionality A
  });

  it('should verify critical functionality B works', () => {
    // Test steps for functionality B
  });

  // Additional test cases...
});
```
`// Example of an automated sanity test script
describe('Sanity Test Suite', () => {
  it('should verify critical functionality A works', () => {
    // Test steps for functionality A
  });

  it('should verify critical functionality B works', () => {
    // Test steps for functionality B
  });

  // Additional test cases...
});`
Automated sanity tests are typically integrated into the CI/CD pipeline to run after each build deployment. Results are documented intest reportsgenerated by the automation framework or CI tool, which are then reviewed to make decisions about the stability of the build.
[test reports](/wiki/test-report)
Determining which functionalities to test insanity testinginvolves focusing on the most critical aspects of the software that have been recently modified or impacted by code changes. To select these functionalities, consider the following criteria:
**sanity testing**[sanity testing](/wiki/sanity-testing)- RecentBugFixes: Prioritize functionalities that have undergone recent bug fixes to ensure the fixes are effective and have not introduced new issues.
- New Features: Test new features that are critical for the application's operation and are likely to be used frequently by end-users.
- High-Risk Areas: Identify areas of the application that are prone to errors or have a history of issues, as these are more likely to break with new changes.
- Core Functionalities: Focus on the core functionalities that are essential for the application to run smoothly, as any issues here can render the software unusable.
- Dependencies: Consider functionalities that have dependencies on the modified code, as changes can have cascading effects on related features.
**RecentBugFixes**[Bug](/wiki/bug)**New Features****High-Risk Areas****Core Functionalities****Dependencies**
Use a risk-based approach to prioritize testing efforts, ensuring that the most impactful and critical areas are covered. Collaborate with developers, product managers, and other stakeholders to understand the scope of changes and their potential impact on the application. This collaboration helps in creating a targeted sanitytest suitethat is both efficient and effective.
[test suite](/wiki/test-suite)
The typical duration of asanity testvaries depending on the scope of the changes made to the software and the size of the project. Generally, sanity tests are brief, often taking anywhere from15 minutes to a few hoursto execute. These tests are designed to be quick checks to ensure that the most crucial functions work as expected after minor modifications.
**sanity test****15 minutes to a few hours**
Sincesanity testingis a subset ofregression testing, it focuses on specific areas rather than the entire application. The duration is kept short to facilitate rapid feedback to the development team. In acontinuous integrationenvironment, sanity tests may run even faster, as they are automated and executed as soon as a new build is available.
[sanity testing](/wiki/sanity-testing)[regression testing](/wiki/regression-testing)**continuous integration**
For experiencedtest automationengineers, it's essential to have a well-optimized suite of sanity tests that can be triggered automatically. This suite should be concise yet comprehensive enough to cover the critical functionalities that could be affected by recent code changes. The speed of execution can be further enhanced by parallel execution and efficienttest managementpractices.
[test automation](/wiki/test-automation)[test management](/wiki/test-management)
Remember, the goal ofsanity testingis to quickly determine whether it's reasonable to proceed with further, more exhaustive testing. Therefore, the duration should align with this objective, ensuring a balance between thoroughness and time efficiency.
[sanity testing](/wiki/sanity-testing)
In acontinuous integration (CI)environment,sanity testingis typically automated and integrated into the CI pipeline. The process is as follows:
**continuous integration (CI)**[sanity testing](/wiki/sanity-testing)1. Code Commit: Developers push code to the repository, triggering the CI pipeline.
2. Build: The CI server compiles the code into an executable application.
3. Deploy: The build is deployed to a test environment automatically.
4. SanityTest Suite: A predefined suite of sanity tests is executed. These tests are a subset of the regression suite, focusing on critical functionalities.
5. Test Execution: Automated scripts run the sanity tests. These scripts are often written in a high-level language and managed by a test framework.
6. Results Analysis: Test results are automatically collected and analyzed. Failures halt the pipeline, and stakeholders are notified.
7. Feedback Loop: Developers receive immediate feedback on the build's sanity, allowing for quick fixes if necessary.
**Code Commit****Build****Deploy****SanityTest Suite**[Test Suite](/wiki/test-suite)**Test Execution**[Test Execution](/wiki/test-execution)**Results Analysis****Feedback Loop**
```
// Example of a sanity test script in TypeScript
import { expect } from 'chai';
import { login, getUserProfile } from './appActions';

describe('Sanity Test Suite', () => {
  it('should successfully log in and retrieve user profile', async () => {
    const loginResponse = await login('user', 'password');
    expect(loginResponse).to.be.true;

    const profile = await getUserProfile();
    expect(profile).to.have.property('username');
  });
});
```
`// Example of a sanity test script in TypeScript
import { expect } from 'chai';
import { login, getUserProfile } from './appActions';

describe('Sanity Test Suite', () => {
  it('should successfully log in and retrieve user profile', async () => {
    const loginResponse = await login('user', 'password');
    expect(loginResponse).to.be.true;

    const profile = await getUserProfile();
    expect(profile).to.have.property('username');
  });
});`
Automated sanity tests are designed to befastandfocused, providing a quick check to ensure that the most crucial parts of the application are functioning after each build. Results are typically logged into atest managementtool or directly into the CI system for easy access and review.
**fast****focused**[test management](/wiki/test-management)
#### Tools and Practices
- What tools are commonly used for sanity testing?Common tools forsanity testinginclude:Selenium: A popular framework for web applications that supports multiple languages and browsers.Appium: Extends Selenium's framework to mobile applications.TestComplete: Offers a user-friendly interface and scripting languages for automated testing.JUnit(for Java) andNUnit(for .NET): Frameworks for unit testing that can be adapted for sanity checks.Postman: For API sanity testing, allowing quick checks on RESTful services.QTP/UFT: A versatile tool from Micro Focus for functional and regression testing.Rational Functional Tester: IBM's solution for automated functional and regression testing.Cypress: A modern end-to-end testing framework designed for web applications.Robot Framework: A keyword-driven test automation framework for acceptance testing and acceptance test-driven development (ATDD).These tools can be integrated intoCI/CD pipelinesto execute sanity tests automatically after each build. Scripts are typically written in the language supported by the tool, such as Python, Java, or JavaScript.// Example of a simple sanity check using Selenium WebDriver in JavaScript
const { Builder, By } = require('selenium-webdriver');
(async function example() {
    let driver = await new Builder().forBrowser('firefox').build();
    try {
        await driver.get('http://www.example.com');
        const element = await driver.findElement(By.id('important-element'));
        if (element.isDisplayed()) {
            console.log('Sanity test passed.');
        } else {
            console.log('Sanity test failed.');
        }
    } finally {
        await driver.quit();
    }
})();Automation scripts forsanity testingare oftenspecific to the releaseor build being tested, focusing on critical functionalities that were recently modified.
- How can automation be incorporated into sanity testing?Incorporating automation intosanity testingcan streamline the process and ensure that critical functionalities work as expected after minor changes. To automate sanity tests, follow these steps:Identify critical pathsthat are stable and unlikely to change frequently. These should be the focus of your sanity suite.Create automatedtest scriptsfor these critical functionalities using a preferred test automation tool.Integrate with a CI/CD pipelineto trigger the sanity suite post-build or after deployment to a staging environment.Useassertionsto validate the expected outcomes of the tests.Prioritize speed and stabilityin your tests to quickly assess the health of the application.Maintain and updatethe test suite as necessary to adapt to any changes in the application's critical paths.// Example of a simple automated sanity test script
describe('Sanity Test', () => {
  it('should login successfully with valid credentials', async () => {
    await navigateToLoginPage();
    await enterCredentials('user@example.com', 'password123');
    await submitLoginForm();
    expect(await isLoggedIn()).toBe(true);
  });
});Ensure that the automated sanity tests areself-containedandindependentto avoid cascading failures. Regularlyreview and refinethe suite to discard obsolete tests and add new ones for recent features. By automatingsanity testing, you can achieve faster feedback loops and more efficient use of testing resources.
- What are some best practices for effective sanity testing?To ensure effectivesanity testing, follow these best practices:Prioritize critical pathsby focusing on the most important features and functionalities that have undergone recent changes.Maintain a checklistof sanity test cases to streamline the process and ensure consistency across test cycles.Keep tests simpleand straightforward, avoiding complex scenarios that are better suited for comprehensive testing phases.Automate where possibleto speed up the process and enable frequent re-running of sanity tests, especially in a CI/CD pipeline.Use version controlfor your sanity test scripts to track changes and facilitate collaboration among team members.Validate fixesand new features quickly to confirm they work as expected without introducing new issues.Isolatetest environmentto ensure that the sanity testing is not affected by external factors and provides reliable results.Document resultsconcisely, focusing on pass/fail status and critical observations that require immediate attention.Communicate effectivelywith the development team to quickly address any issues found during sanity testing.Review and updateyour sanity test suite regularly to reflect changes in the application and to remove obsolete or redundant tests.By adhering to these practices, you can maximize the efficiency and effectiveness of yoursanity testingefforts, ensuring that the software is stable and ready for further testing or release.
- Can sanity tests be reused or are they typically unique for each software version?Sanity tests can often bereusedacross different software versions, especially when the changes between versions are incremental and do not significantly affect the areas of functionality that the sanity tests cover. These tests are designed to quickly evaluate whether the core functionalities are working as expected after minor changes orbugfixes.However, when a new feature is introduced or significant changes are made to the existing functionality, sanity tests may need to beupdated or rewrittento reflect the new context. It's essential to review the scope of the changes in each release and adjust the sanity tests accordingly to ensure they remain relevant and effective.In practice, maintaining amodular and flexibletest suitecan facilitate the reuse of sanity tests. By designing tests that are independent and can be easily combined, you can mix and matchtest casesto create an appropriate sanitytest suitefor each version of the software.Automation plays a key role in enabling the reuse of sanity tests. Automated tests can be quicklyadapted and executed, saving time and effort compared tomanual testing. It's crucial to keep the automation code well-organized and to use version control to manage changes to thetest scripts.In summary, while sanity tests can be reused across software versions, they should beregularly reviewed and updatedto ensure they align with the current state of the application and provide meaningful feedback on its sanity.
- How do you document the results of a sanity test?Documenting the results of a sanity test should bestraightforwardandconcise. Follow these guidelines:Summarize the outcome: Begin with a clear statement indicating whether the sanity test passed or failed.List tested functionalities: Provide a bullet-point list of the specific functionalities checked.Detail failures: For any failed tests, include a brief description of the issue, steps to reproduce, and any relevant screenshots or error messages.Referencetest cases: Link to detailed test cases or scripts used for the sanity test, if applicable.Include environment details: Note the testing environment, software version, and configuration.Recordtest data: Mention any specific data sets used, which can be critical for reproducing issues.State impact: Assess the impact of any failures on the overall system.Recommendations: Offer immediate recommendations or actions taken, such as filing bug reports or halting a release.Use Markdown for formatting:- **Outcome**: Passed/Failed
- **Functionalities Tested**:
  - Login process
  - Payment gateway integration
  - New user registration
- **Failures**:
  - Payment gateway integration: Timeout error when processing payments. Steps to reproduce: [Link to test case]. Screenshot: ![Error Screenshot](url).
- **Environment**: Windows 10, Software v2.3.1, Test Environment B
- **Test Data Used**: Test Credit Card #1234
- **Impact**: Payment processing critical for release. Failure blocks release.
- **Recommendations**: Bug reported (ID #98765), suggest rollback to previous stable version.Ensure the documentation isup-to-dateandaccessibleto all relevant team members.

Common tools forsanity testinginclude:
**sanity testing**[sanity testing](/wiki/sanity-testing)- Selenium: A popular framework for web applications that supports multiple languages and browsers.
- Appium: Extends Selenium's framework to mobile applications.
- TestComplete: Offers a user-friendly interface and scripting languages for automated testing.
- JUnit(for Java) andNUnit(for .NET): Frameworks for unit testing that can be adapted for sanity checks.
- Postman: For API sanity testing, allowing quick checks on RESTful services.
- QTP/UFT: A versatile tool from Micro Focus for functional and regression testing.
- Rational Functional Tester: IBM's solution for automated functional and regression testing.
- Cypress: A modern end-to-end testing framework designed for web applications.
- Robot Framework: A keyword-driven test automation framework for acceptance testing and acceptance test-driven development (ATDD).
**Selenium**[Selenium](/wiki/selenium)**Appium****TestComplete****JUnit****NUnit**[NUnit](/wiki/nunit)**Postman**[Postman](/wiki/postman)**QTP/UFT****Rational Functional Tester****Cypress**[Cypress](/wiki/cypress)**Robot Framework**
These tools can be integrated intoCI/CD pipelinesto execute sanity tests automatically after each build. Scripts are typically written in the language supported by the tool, such as Python, Java, or JavaScript.
**CI/CD pipelines**
```
// Example of a simple sanity check using Selenium WebDriver in JavaScript
const { Builder, By } = require('selenium-webdriver');
(async function example() {
    let driver = await new Builder().forBrowser('firefox').build();
    try {
        await driver.get('http://www.example.com');
        const element = await driver.findElement(By.id('important-element'));
        if (element.isDisplayed()) {
            console.log('Sanity test passed.');
        } else {
            console.log('Sanity test failed.');
        }
    } finally {
        await driver.quit();
    }
})();
```
`// Example of a simple sanity check using Selenium WebDriver in JavaScript
const { Builder, By } = require('selenium-webdriver');
(async function example() {
    let driver = await new Builder().forBrowser('firefox').build();
    try {
        await driver.get('http://www.example.com');
        const element = await driver.findElement(By.id('important-element'));
        if (element.isDisplayed()) {
            console.log('Sanity test passed.');
        } else {
            console.log('Sanity test failed.');
        }
    } finally {
        await driver.quit();
    }
})();`
Automation scripts forsanity testingare oftenspecific to the releaseor build being tested, focusing on critical functionalities that were recently modified.
[sanity testing](/wiki/sanity-testing)**specific to the release**
Incorporating automation intosanity testingcan streamline the process and ensure that critical functionalities work as expected after minor changes. To automate sanity tests, follow these steps:
[sanity testing](/wiki/sanity-testing)1. Identify critical pathsthat are stable and unlikely to change frequently. These should be the focus of your sanity suite.
2. Create automatedtest scriptsfor these critical functionalities using a preferred test automation tool.
3. Integrate with a CI/CD pipelineto trigger the sanity suite post-build or after deployment to a staging environment.
4. Useassertionsto validate the expected outcomes of the tests.
5. Prioritize speed and stabilityin your tests to quickly assess the health of the application.
6. Maintain and updatethe test suite as necessary to adapt to any changes in the application's critical paths.
**Identify critical paths****Create automatedtest scripts**[test scripts](/wiki/test-script)**Integrate with a CI/CD pipeline****assertions****Prioritize speed and stability****Maintain and update**
```
// Example of a simple automated sanity test script
describe('Sanity Test', () => {
  it('should login successfully with valid credentials', async () => {
    await navigateToLoginPage();
    await enterCredentials('user@example.com', 'password123');
    await submitLoginForm();
    expect(await isLoggedIn()).toBe(true);
  });
});
```
`// Example of a simple automated sanity test script
describe('Sanity Test', () => {
  it('should login successfully with valid credentials', async () => {
    await navigateToLoginPage();
    await enterCredentials('user@example.com', 'password123');
    await submitLoginForm();
    expect(await isLoggedIn()).toBe(true);
  });
});`
Ensure that the automated sanity tests areself-containedandindependentto avoid cascading failures. Regularlyreview and refinethe suite to discard obsolete tests and add new ones for recent features. By automatingsanity testing, you can achieve faster feedback loops and more efficient use of testing resources.
**self-contained****independent****review and refine**[sanity testing](/wiki/sanity-testing)
To ensure effectivesanity testing, follow these best practices:
[sanity testing](/wiki/sanity-testing)- Prioritize critical pathsby focusing on the most important features and functionalities that have undergone recent changes.
- Maintain a checklistof sanity test cases to streamline the process and ensure consistency across test cycles.
- Keep tests simpleand straightforward, avoiding complex scenarios that are better suited for comprehensive testing phases.
- Automate where possibleto speed up the process and enable frequent re-running of sanity tests, especially in a CI/CD pipeline.
- Use version controlfor your sanity test scripts to track changes and facilitate collaboration among team members.
- Validate fixesand new features quickly to confirm they work as expected without introducing new issues.
- Isolatetest environmentto ensure that the sanity testing is not affected by external factors and provides reliable results.
- Document resultsconcisely, focusing on pass/fail status and critical observations that require immediate attention.
- Communicate effectivelywith the development team to quickly address any issues found during sanity testing.
- Review and updateyour sanity test suite regularly to reflect changes in the application and to remove obsolete or redundant tests.
**Prioritize critical paths****Maintain a checklist****Keep tests simple****Automate where possible****Use version control****Validate fixes****Isolatetest environment**[test environment](/wiki/test-environment)**Document results****Communicate effectively****Review and update**
By adhering to these practices, you can maximize the efficiency and effectiveness of yoursanity testingefforts, ensuring that the software is stable and ready for further testing or release.
[sanity testing](/wiki/sanity-testing)
Sanity tests can often bereusedacross different software versions, especially when the changes between versions are incremental and do not significantly affect the areas of functionality that the sanity tests cover. These tests are designed to quickly evaluate whether the core functionalities are working as expected after minor changes orbugfixes.
**reused**[bug](/wiki/bug)
However, when a new feature is introduced or significant changes are made to the existing functionality, sanity tests may need to beupdated or rewrittento reflect the new context. It's essential to review the scope of the changes in each release and adjust the sanity tests accordingly to ensure they remain relevant and effective.
**updated or rewritten**
In practice, maintaining amodular and flexibletest suitecan facilitate the reuse of sanity tests. By designing tests that are independent and can be easily combined, you can mix and matchtest casesto create an appropriate sanitytest suitefor each version of the software.
**modular and flexible**[test suite](/wiki/test-suite)[test cases](/wiki/test-case)[test suite](/wiki/test-suite)
Automation plays a key role in enabling the reuse of sanity tests. Automated tests can be quicklyadapted and executed, saving time and effort compared tomanual testing. It's crucial to keep the automation code well-organized and to use version control to manage changes to thetest scripts.
**adapted and executed**[manual testing](/wiki/manual-testing)[test scripts](/wiki/test-script)
In summary, while sanity tests can be reused across software versions, they should beregularly reviewed and updatedto ensure they align with the current state of the application and provide meaningful feedback on its sanity.
**regularly reviewed and updated**
Documenting the results of a sanity test should bestraightforwardandconcise. Follow these guidelines:
**straightforward****concise**- Summarize the outcome: Begin with a clear statement indicating whether the sanity test passed or failed.
- List tested functionalities: Provide a bullet-point list of the specific functionalities checked.
- Detail failures: For any failed tests, include a brief description of the issue, steps to reproduce, and any relevant screenshots or error messages.
- Referencetest cases: Link to detailed test cases or scripts used for the sanity test, if applicable.
- Include environment details: Note the testing environment, software version, and configuration.
- Recordtest data: Mention any specific data sets used, which can be critical for reproducing issues.
- State impact: Assess the impact of any failures on the overall system.
- Recommendations: Offer immediate recommendations or actions taken, such as filing bug reports or halting a release.
**Summarize the outcome****List tested functionalities****Detail failures****Referencetest cases**[test cases](/wiki/test-case)**Include environment details****Recordtest data**[test data](/wiki/test-data)**State impact****Recommendations**
Use Markdown for formatting:

```
- **Outcome**: Passed/Failed
- **Functionalities Tested**:
  - Login process
  - Payment gateway integration
  - New user registration
- **Failures**:
  - Payment gateway integration: Timeout error when processing payments. Steps to reproduce: [Link to test case]. Screenshot: ![Error Screenshot](url).
- **Environment**: Windows 10, Software v2.3.1, Test Environment B
- **Test Data Used**: Test Credit Card #1234
- **Impact**: Payment processing critical for release. Failure blocks release.
- **Recommendations**: Bug reported (ID #98765), suggest rollback to previous stable version.
```
`- **Outcome**: Passed/Failed
- **Functionalities Tested**:
  - Login process
  - Payment gateway integration
  - New user registration
- **Failures**:
  - Payment gateway integration: Timeout error when processing payments. Steps to reproduce: [Link to test case]. Screenshot: ![Error Screenshot](url).
- **Environment**: Windows 10, Software v2.3.1, Test Environment B
- **Test Data Used**: Test Credit Card #1234
- **Impact**: Payment processing critical for release. Failure blocks release.
- **Recommendations**: Bug reported (ID #98765), suggest rollback to previous stable version.`
Ensure the documentation isup-to-dateandaccessibleto all relevant team members.
**up-to-date****accessible**
