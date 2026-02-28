# Ad Hoc Testing


<!-- TOC START -->
- [Related Terms:](#related-terms)
- [Questions about Ad Hoc Testing ?](#questions-about-ad-hoc-testing)
  - [Basics and Importance](#basics-and-importance)
    - [What is Ad Hoc testing in software testing?](#what-is-ad-hoc-testing-in-software-testing)
    - [Why is Ad Hoc testing important in the software development lifecycle?](#why-is-ad-hoc-testing-important-in-the-software-development-lifecycle)
    - [What are the key differences between Ad Hoc testing and other forms of testing?](#what-are-the-key-differences-between-ad-hoc-testing-and-other-forms-of-testing)
    - [What are the advantages and disadvantages of Ad Hoc testing?](#what-are-the-advantages-and-disadvantages-of-ad-hoc-testing)
  - [Implementation and Techniques](#implementation-and-techniques)
    - [How is Ad Hoc testing performed?](#how-is-ad-hoc-testing-performed)
    - [What are some common techniques used in Ad Hoc testing?](#what-are-some-common-techniques-used-in-ad-hoc-testing)
    - [What skills are required to effectively perform Ad Hoc testing?](#what-skills-are-required-to-effectively-perform-ad-hoc-testing)
    - [Can Ad Hoc testing be automated or is it strictly manual?](#can-ad-hoc-testing-be-automated-or-is-it-strictly-manual)
  - [Scenarios and Use Cases](#scenarios-and-use-cases)
    - [What are some real-world examples of when Ad Hoc testing would be used?](#what-are-some-real-world-examples-of-when-ad-hoc-testing-would-be-used)
    - [Can you provide a scenario where Ad Hoc testing identified a critical bug?](#can-you-provide-a-scenario-where-ad-hoc-testing-identified-a-critical-bug)
    - [How does Ad Hoc testing fit into end-to-end (e2e) testing scenarios?](#how-does-ad-hoc-testing-fit-into-end-to-end-e2e-testing-scenarios)
  - [Best Practices](#best-practices)
    - [What are some best practices for conducting Ad Hoc testing?](#what-are-some-best-practices-for-conducting-ad-hoc-testing)
    - [How can the effectiveness of Ad Hoc testing be measured?](#how-can-the-effectiveness-of-ad-hoc-testing-be-measured)
    - [How can Ad Hoc testing be integrated into a continuous integration/continuous deployment (CI/CD) pipeline?](#how-can-ad-hoc-testing-be-integrated-into-a-continuous-integrationcontinuous-deployment-cicd-pipeline)
<!-- TOC END -->

Ad hoc testing

is an informal, spontaneous approach to

software testing

. Its main objective is to identify vulnerabilities or issues as quickly as possible. This method is unstructured, conducted without detailed planning or documentation.

## Related Terms:

- [Exploratory Testing](../E/exploratory-testing.md)

## Questions about Ad Hoc Testing ?

### Basics and Importance

#### What is Ad Hoc testing in software testing?

  [Ad Hoc testing](../A/ad-hoc-testing.md) is an informal and unstructured testing technique where testers explore the software without any specific plans or documentation. It relies on the tester's intuition, experience, and understanding of the application to guide the testing process. This type of testing is often used to discover defects that may not be found through traditional, structured testing methods.
  In [Ad Hoc testing](../A/ad-hoc-testing.md), testers are free to take any path through the application and use any valid or invalid input data they choose. It's a type of [exploratory testing](../E/exploratory-testing.md) where the primary goal is to find [bugs](../B/bug.md) by thinking outside the box and trying to break the system in creative ways.
  Since [Ad Hoc testing](../A/ad-hoc-testing.md) is unscripted, it can be difficult to reproduce issues unless the tester has taken detailed notes about their actions. It's typically used in the later stages of testing after formal [test cases](../T/test-case.md) have been executed, to supplement more structured testing methods.
  **Key Points:**

  - **Unstructured**
    and
    **informal**
    testing method.

  - Relies on tester's
    **intuition**
    and
    **experience**
    .

  - Used to find defects not caught by structured testing.
  - Allows for
    **creative**
    and
    **unconstrained**
    exploration.

  - Difficult to reproduce issues without detailed notes.
  - Complements structured testing in later stages.
  - **Unstructured**
    and
    **informal**
    testing method.

  - Relies on tester's
    **intuition**
    and
    **experience**
    .

  - Used to find defects not caught by structured testing.
  - Allows for
    **creative**
    and
    **unconstrained**
    exploration.

  - Difficult to reproduce issues without detailed notes.
  - Complements structured testing in later stages.

#### Why is Ad Hoc testing important in the software development lifecycle?

  [Ad Hoc testing](../A/ad-hoc-testing.md) is crucial in the **software development lifecycle** (SDLC) because it offers a unique approach to uncovering defects that structured testing might miss. It relies on the tester's intuition, experience, and understanding of the system to explore the application without predefined [test cases](../T/test-case.md) or documentation. This can lead to the discovery of **unexpected issues**, particularly in complex or less well-understood areas of the application.
  Since [Ad Hoc testing](../A/ad-hoc-testing.md) is unscripted, it allows testers to **simulate a user's perspective** more naturally, potentially identifying usability problems that formal [test cases](../T/test-case.md) wouldn't. It's also valuable for **[stress testing](../S/stress-testing.md)** an application in ways that weren't anticipated during the design phase.
  Incorporating [Ad Hoc testing](../A/ad-hoc-testing.md) into the SDLC enhances the overall **[test coverage](../T/test-coverage.md)** and provides a complementary method to structured testing. It's especially important in the later stages of development, after formal test cycles have been completed, to perform a final check before releases or to quickly test patches and minor updates.
  Moreover, [Ad Hoc testing](../A/ad-hoc-testing.md) can be a **time-efficient** way to test the application when deadlines are tight, as it requires no upfront preparation. It's a flexible testing method that can be used whenever there is an opportunity, making it a valuable tool for continuous improvement in the SDLC.

#### What are the key differences between Ad Hoc testing and other forms of testing?

  [Ad Hoc testing](../A/ad-hoc-testing.md) differs from other forms of testing primarily in its **lack of formal structure** and **predefined [test cases](../T/test-case.md)**. Unlike systematic testing methods such as unit, integration, or [system testing](../S/system-testing.md), [Ad Hoc testing](../A/ad-hoc-testing.md) is **unscripted** and relies on the tester's intuition, experience, and understanding of the system to explore the application and find defects.
  Other forms of testing often follow a **documented process** and are based on **[test plans](../T/test-plan.md)**, **[test cases](../T/test-case.md)**, and **[test scripts](../T/test-script.md)** that are designed in advance. These tests are typically **repeatable** and can be **automated**, ensuring consistent coverage across test cycles.
  In contrast, [Ad Hoc testing](../A/ad-hoc-testing.md) is **spontaneous** and **informal**, making it **non-repeatable**. It is primarily a **manual** testing process, as it requires human creativity and insight to execute. Testers performing [Ad Hoc testing](../A/ad-hoc-testing.md) may focus on areas of the application that are **difficult to automate** or require **human judgment**.
  While other testing methods aim for comprehensive coverage through detailed [test scenarios](../T/test-scenario.md), [Ad Hoc testing](../A/ad-hoc-testing.md) is often used to discover **edge cases** or **unusual defects** that structured tests might miss. It is typically employed when there is **limited time** and as a complement to other testing strategies, rather than as a standalone approach.
  [Ad Hoc testing](../A/ad-hoc-testing.md)'s flexibility allows testers to **quickly adapt** to the application's changes without the need to update formal test documentation. However, due to its unstructured nature, it can be **challenging to track** and **measure its effectiveness** compared to more formalized testing methods.

#### What are the advantages and disadvantages of Ad Hoc testing?

  Advantages of [Ad Hoc Testing](../A/ad-hoc-testing.md):

  - **Flexibility** : Allows testers to explore the application without predefined cases, encouraging creative test scenarios.
  - **Cost-effective** : No need for extensive preparation or documentation, reducing initial costs.
  - **Quick Feedback** : Provides immediate insights into the application's functionality and potential issues.
  - **Uncover Unexpected [Bugs](../B/bug.md)** : Can reveal defects that structured testing might miss due to its unpredictable nature.
  Disadvantages of [Ad Hoc Testing](../A/ad-hoc-testing.md):

  - **Non-reproducible** : Finding a bug might be a one-time event if the steps aren't documented, making it hard to track and fix.
  - **Lack of Coverage** : Without a structured approach, some parts of the application might remain untested.
  - **Subjective Results** : Heavily relies on the tester's expertise and intuition, which can lead to inconsistent outcomes.
  - **Not Suitable for All Stages** : May not be effective in later stages of development where more formal verification is required.
  Remember, [Ad Hoc testing](../A/ad-hoc-testing.md) is a complement to other testing methods, not a standalone solution. It's most effective when used by **experienced testers** who can quickly identify and explore complex application areas.

  - **Flexibility** : Allows testers to explore the application without predefined cases, encouraging creative test scenarios.
  - **Cost-effective** : No need for extensive preparation or documentation, reducing initial costs.
  - **Quick Feedback** : Provides immediate insights into the application's functionality and potential issues.
  - **Uncover Unexpected [Bugs](../B/bug.md)** : Can reveal defects that structured testing might miss due to its unpredictable nature.
  - **Non-reproducible** : Finding a bug might be a one-time event if the steps aren't documented, making it hard to track and fix.
  - **Lack of Coverage** : Without a structured approach, some parts of the application might remain untested.
  - **Subjective Results** : Heavily relies on the tester's expertise and intuition, which can lead to inconsistent outcomes.
  - **Not Suitable for All Stages** : May not be effective in later stages of development where more formal verification is required.

### Implementation and Techniques

#### How is Ad Hoc testing performed?

  [Ad Hoc testing](../A/ad-hoc-testing.md) is performed **without any formal test planning** or documentation. Testers dive into the application with their understanding and **explore the software** to find defects. This approach relies heavily on the tester's **intuition, experience, and creativity**.
  Here's a general process for performing [Ad Hoc testing](../A/ad-hoc-testing.md):

  1. **Understand the Application** : Gain a basic understanding of the software's functionality and purpose.
  2. **Define a Scope** : Even though it's informal, decide on the areas of the application to focus on.
  3. **Execute Tests** : Interact with the software in various ways to uncover issues, including:
    - Trying out different inputs
    - Navigating through the application in unexpected ways
    - Attempting to break the application with unusual behavior
    - Trying out different inputs
    - Navigating through the application in unexpected ways
    - Attempting to break the application with unusual behavior
  4. **Note Observations** : Keep track of any defects or strange behaviors observed during testing.
  5. **Report [Bugs](../B/bug.md)** : Communicate found issues to the development team for resolution.
  During [Ad Hoc testing](../A/ad-hoc-testing.md), testers may employ techniques like **[error guessing](../E/error-guessing.md)** or **[exploratory testing](../E/exploratory-testing.md)** to guide their approach. The process is inherently **flexible and unstructured**, allowing testers to rapidly identify issues that structured testing might miss.
  It's important to note that while [Ad Hoc testing](../A/ad-hoc-testing.md) can be spontaneous, having a **broad knowledge of the system** and its potential weak points can lead to more effective testing sessions.

  1. **Understand the Application** : Gain a basic understanding of the software's functionality and purpose.
  2. **Define a Scope** : Even though it's informal, decide on the areas of the application to focus on.
  3. **Execute Tests** : Interact with the software in various ways to uncover issues, including:
    - Trying out different inputs
    - Navigating through the application in unexpected ways
    - Attempting to break the application with unusual behavior
    - Trying out different inputs
    - Navigating through the application in unexpected ways
    - Attempting to break the application with unusual behavior
  4. **Note Observations** : Keep track of any defects or strange behaviors observed during testing.
  5. **Report [Bugs](../B/bug.md)** : Communicate found issues to the development team for resolution.

#### What are some common techniques used in Ad Hoc testing?

  Common techniques in **[Ad Hoc testing](../A/ad-hoc-testing.md)** include:

  - **[Exploratory Testing](../E/exploratory-testing.md)** : Testers explore the software without predefined test cases, using their understanding and intuition to guide their actions.
  - **[Error Guessing](../E/error-guessing.md)** : Testers rely on experience to guess the most probable areas of the software where defects might occur.
  - **[Monkey Testing](../M/monkey-testing.md)** : Random inputs are provided to the system to see how it behaves, often automated to generate large volumes of random data.
  - **[Pair Testing](../P/pair-testing.md)** : Two testers work together at one keyboard; one operates the testing while the other provides guidance and records findings.
  - **[Session-Based Testing](../S/session-based-testing.md)** : Testing is structured into uninterrupted sessions focused on a particular area, with testers documenting their findings and thought processes.
  These techniques are often used in a **complementary** manner, depending on the context and goals of the testing session. They leverage the tester's creativity, experience, and intuition to uncover issues that structured testing might miss.

  - **[Exploratory Testing](../E/exploratory-testing.md)** : Testers explore the software without predefined test cases, using their understanding and intuition to guide their actions.
  - **[Error Guessing](../E/error-guessing.md)** : Testers rely on experience to guess the most probable areas of the software where defects might occur.
  - **[Monkey Testing](../M/monkey-testing.md)** : Random inputs are provided to the system to see how it behaves, often automated to generate large volumes of random data.
  - **[Pair Testing](../P/pair-testing.md)** : Two testers work together at one keyboard; one operates the testing while the other provides guidance and records findings.
  - **[Session-Based Testing](../S/session-based-testing.md)** : Testing is structured into uninterrupted sessions focused on a particular area, with testers documenting their findings and thought processes.

#### What skills are required to effectively perform Ad Hoc testing?

  To effectively perform **[Ad Hoc testing](../A/ad-hoc-testing.md)**, an individual needs a blend of skills that enable them to explore the software without a predefined [test plan](../T/test-plan.md). These include:

  - **Exploratory Skills** : Ability to creatively explore and navigate the software to uncover issues that structured testing might miss.
  - **Analytical Skills** : Strong analytical thinking to hypothesize where bugs may exist and to understand the software's behavior.
  - **Attention to Detail** : Keen observation to notice minor discrepancies and potential issues that could lead to larger problems.
  - **Technical Knowledge** : A solid understanding of the software's architecture, features, and potential weak points.
  - **Experience** : Familiarity with the system under test and similar systems to draw upon past knowledge and identify patterns.
  - **Intuition** : An intuitive sense of where bugs are likely to occur, often developed from experience.
  - **Communication Skills** : Ability to clearly document and communicate findings to the development team and other stakeholders.
  - **Adaptability** : Flexibility to switch focus and adapt to new information or areas of concern as they arise during testing.
  - **Time Management** : Skill to manage time effectively, as Ad Hoc testing is often time-boxed or performed in limited time frames.
  These skills help testers to perform **[Ad Hoc testing](../A/ad-hoc-testing.md)** in a manner that is both efficient and effective, providing valuable insights into the software's quality and reliability.

  - **Exploratory Skills** : Ability to creatively explore and navigate the software to uncover issues that structured testing might miss.
  - **Analytical Skills** : Strong analytical thinking to hypothesize where bugs may exist and to understand the software's behavior.
  - **Attention to Detail** : Keen observation to notice minor discrepancies and potential issues that could lead to larger problems.
  - **Technical Knowledge** : A solid understanding of the software's architecture, features, and potential weak points.
  - **Experience** : Familiarity with the system under test and similar systems to draw upon past knowledge and identify patterns.
  - **Intuition** : An intuitive sense of where bugs are likely to occur, often developed from experience.
  - **Communication Skills** : Ability to clearly document and communicate findings to the development team and other stakeholders.
  - **Adaptability** : Flexibility to switch focus and adapt to new information or areas of concern as they arise during testing.
  - **Time Management** : Skill to manage time effectively, as Ad Hoc testing is often time-boxed or performed in limited time frames.

#### Can Ad Hoc testing be automated or is it strictly manual?

  [Ad Hoc testing](../A/ad-hoc-testing.md), by its very nature, is an informal and unstructured approach to testing where the tester actively explores the software without predefined [test cases](../T/test-case.md) or plans. Automation, on the other hand, relies on pre-scripted tests that run automatically. Therefore, **[Ad Hoc testing](../A/ad-hoc-testing.md) is predominantly a manual process**.
  However, certain aspects of [Ad Hoc testing](../A/ad-hoc-testing.md) can be supported by automation tools. For instance, automated scripts can be used to set up complex environments or states within the application, which testers can then explore manually. This hybrid approach allows testers to focus on the exploratory aspect of [Ad Hoc testing](../A/ad-hoc-testing.md) without the overhead of repetitive [setup](../S/setup.md) tasks.
  Additionally, while the exploratory part of [Ad Hoc testing](../A/ad-hoc-testing.md) is manual, **automation can assist in logging and capturing the state of the system** when an issue is discovered. Tools can automatically record the steps taken, system state, and other relevant data, aiding in [bug](../B/bug.md) reproduction and reporting.
  In summary, while the core activity of [Ad Hoc testing](../A/ad-hoc-testing.md) is manual, automation can play a supportive role in enhancing the efficiency and effectiveness of the testing process.

### Scenarios and Use Cases

#### What are some real-world examples of when Ad Hoc testing would be used?

  [Ad Hoc testing](../A/ad-hoc-testing.md) is often employed in situations where there is limited structure or documentation, and a quick, intuitive assessment of the software's behavior is needed. Here are some real-world examples:

  - **[Exploratory Testing](../E/exploratory-testing.md)** : When a new feature is developed, testers may use Ad Hoc methods to explore the feature's functionality before formal test cases are written.
  - **Post-Release** : After a software release, Ad Hoc testing can be used to perform a quick check on the live environment to ensure that no major issues have been introduced.
  - **[Bug](../B/bug.md) [Verification](../V/verification.md)** : Once a bug has been fixed, testers might conduct Ad Hoc testing around the fix to ensure the issue is resolved and no new issues have been introduced.
  - **High-Risk Areas** : In a system with known high-risk components, Ad Hoc testing can be used to quickly assess the stability of these areas, especially after changes have been made.
  - **Limited Time** : When there is a time constraint and formal testing cannot be completed, Ad Hoc testing can provide a quick sanity check to assess critical functionalities.
  - **User Feedback** : If users report unexpected behavior, testers might use Ad Hoc testing to replicate the issue and explore related functionalities that might be affected.
  - **Technology Changes** : When underlying technology or frameworks are updated, Ad Hoc testing can help in quickly identifying any compatibility issues or regressions.
  In these scenarios, the tester's experience, intuition, and knowledge of the system guide the testing process, often leading to the discovery of defects that structured testing might overlook.

  - **[Exploratory Testing](../E/exploratory-testing.md)** : When a new feature is developed, testers may use Ad Hoc methods to explore the feature's functionality before formal test cases are written.
  - **Post-Release** : After a software release, Ad Hoc testing can be used to perform a quick check on the live environment to ensure that no major issues have been introduced.
  - **[Bug](../B/bug.md) [Verification](../V/verification.md)** : Once a bug has been fixed, testers might conduct Ad Hoc testing around the fix to ensure the issue is resolved and no new issues have been introduced.
  - **High-Risk Areas** : In a system with known high-risk components, Ad Hoc testing can be used to quickly assess the stability of these areas, especially after changes have been made.
  - **Limited Time** : When there is a time constraint and formal testing cannot be completed, Ad Hoc testing can provide a quick sanity check to assess critical functionalities.
  - **User Feedback** : If users report unexpected behavior, testers might use Ad Hoc testing to replicate the issue and explore related functionalities that might be affected.
  - **Technology Changes** : When underlying technology or frameworks are updated, Ad Hoc testing can help in quickly identifying any compatibility issues or regressions.

#### Can you provide a scenario where Ad Hoc testing identified a critical bug?

  Scenario: During a late-stage development sprint, a test engineer was exploring a newly implemented feature in a financial application that allowed users to transfer funds between accounts. The formal [test cases](../T/test-case.md) had already been executed, and no significant issues were found. However, the engineer decided to perform some **[Ad Hoc testing](../A/ad-hoc-testing.md)** by mimicking a user who might make erratic and unconventional choices.
  While randomly navigating the application, the engineer attempted to initiate a transfer from an account with insufficient funds, expecting the standard error message. Instead, the application crashed, and upon restart, the account balances were corrupted, displaying incorrect figures.
  This critical [bug](../B/bug.md) had eluded structured testing because the [test cases](../T/test-case.md) assumed rational user behavior and did not account for the specific sequence of actions the engineer took during the Ad Hoc session. The [bug](../B/bug.md) was a result of an unhandled exception when processing transactions with specific timing and data conditions that were not covered in the [test scripts](../T/test-script.md).
  The discovery of this [bug](../B/bug.md) was significant because it could have led to severe financial discrepancies in a production environment. The [Ad Hoc testing](../A/ad-hoc-testing.md) approach allowed the engineer to uncover a critical issue that structured testing missed, demonstrating the value of this testing method in identifying unpredictable, real-world problems.

#### How does Ad Hoc testing fit into end-to-end (e2e) testing scenarios?

  [Ad Hoc testing](../A/ad-hoc-testing.md), while primarily manual and exploratory, complements end-to-end (E2E) testing by uncovering issues that structured tests may miss. In E2E scenarios, [Ad Hoc testing](../A/ad-hoc-testing.md) can be strategically employed **after** formal [test cases](../T/test-case.md) have been executed to simulate real-world usage. It's a way to **validate the overall system behavior** and **user experience** without predefined scripts.
  Imagine an E2E test that covers a typical user flow through an application. Once automation confirms that the flow works as expected, [Ad Hoc testing](../A/ad-hoc-testing.md) steps in to probe the edges of the [use case](../U/use-case.md). Testers might try **unexpected input combinations**, **navigate in non-linear paths**, or **stress the system** beyond typical usage patterns. This can reveal vulnerabilities like memory leaks, handling of edge cases, or UI inconsistencies across different devices.
  While [Ad Hoc testing](../A/ad-hoc-testing.md) is not the main focus in E2E scenarios, it's a valuable tool for a **holistic assessment**. It's about thinking like an end user who is not constrained by [test scripts](../T/test-script.md). Automation engineers can benefit from this approach by using insights from Ad Hoc sessions to **enhance automated suites** with more robust [test cases](../T/test-case.md).
  Incorporating Ad Hoc findings into automated E2E tests ensures that the **automation remains relevant** and **adapts to real-world complexities**. It's a cycle of continuous improvement where [Ad Hoc testing](../A/ad-hoc-testing.md) informs automation, and automation frees up time for more [exploratory testing](../E/exploratory-testing.md).

### Best Practices

#### What are some best practices for conducting Ad Hoc testing?

  Best practices for conducting [Ad Hoc testing](../A/ad-hoc-testing.md) include:

  - **Prioritize areas with high risk or changes** : Focus on parts of the application that have undergone recent modifications or are known to be error-prone.
  - **Leverage domain knowledge** : Use your understanding of the business and user behavior to explore functionalities that are critical to the end-user.
  - **Document findings** : While Ad Hoc testing is unscripted, it's important to keep notes on what was tested and any issues discovered for future reference and bug tracking.
  - **Use varied testing techniques** : Combine different approaches like exploratory testing, error guessing, and pair testing to uncover a wide range of issues.
  - **Timebox sessions** : Set a specific duration for Ad Hoc testing to maintain focus and productivity.
  - **Collaborate with others** : Pair up with different team members to gain fresh perspectives and uncover more defects.
  - **Repeat testing** : Conduct Ad Hoc testing at different stages of development to catch new issues that may arise after changes in the code.
  - **Integrate with formal testing** : Use insights from Ad Hoc testing to enhance your formal test cases and automation scripts.
  Remember, while [Ad Hoc testing](../A/ad-hoc-testing.md) is informal, it should still be strategic and targeted to maximize its effectiveness in identifying potential defects.

  - **Prioritize areas with high risk or changes** : Focus on parts of the application that have undergone recent modifications or are known to be error-prone.
  - **Leverage domain knowledge** : Use your understanding of the business and user behavior to explore functionalities that are critical to the end-user.
  - **Document findings** : While Ad Hoc testing is unscripted, it's important to keep notes on what was tested and any issues discovered for future reference and bug tracking.
  - **Use varied testing techniques** : Combine different approaches like exploratory testing, error guessing, and pair testing to uncover a wide range of issues.
  - **Timebox sessions** : Set a specific duration for Ad Hoc testing to maintain focus and productivity.
  - **Collaborate with others** : Pair up with different team members to gain fresh perspectives and uncover more defects.
  - **Repeat testing** : Conduct Ad Hoc testing at different stages of development to catch new issues that may arise after changes in the code.
  - **Integrate with formal testing** : Use insights from Ad Hoc testing to enhance your formal test cases and automation scripts.

#### How can the effectiveness of Ad Hoc testing be measured?

  Measuring the effectiveness of **[Ad Hoc testing](../A/ad-hoc-testing.md)** can be challenging due to its unstructured nature. However, certain metrics can be used to gauge its impact:

  - **Number of [Bugs](../B/bug.md) Found** : Track the bugs identified specifically through Ad Hoc testing, especially those missed by other testing methods.
  - **[Severity](../S/severity.md) of [Bugs](../B/bug.md)** : Evaluate the severity of the defects discovered. High-severity bugs can indicate the effectiveness of Ad Hoc testing in uncovering critical issues.
  - **[Test Coverage](../T/test-coverage.md)** : Although difficult to quantify in Ad Hoc testing, use code coverage tools post-testing to assess which areas of the application were inadvertently tested.
  - **Time to Discover** : Measure the time it takes to find defects. Ad Hoc testing might uncover certain bugs faster than structured testing.
  - **Cost of [Bugs](../B/bug.md)** : Analyze the cost savings from identifying and fixing bugs early, which can be attributed to the informal and rapid nature of Ad Hoc testing.
  - **Feedback from Testers** : Collect qualitative feedback from testers on the ease of finding defects and their perception of the thoroughness of Ad Hoc testing.
  Use these metrics in conjunction with the context of your testing environment to determine the effectiveness of [Ad Hoc testing](../A/ad-hoc-testing.md). Remember that while these metrics can provide insights, the unscripted nature of [Ad Hoc testing](../A/ad-hoc-testing.md) means that its true value often lies in the tester's expertise and intuition, which can be harder to quantify.

  - **Number of [Bugs](../B/bug.md) Found** : Track the bugs identified specifically through Ad Hoc testing, especially those missed by other testing methods.
  - **[Severity](../S/severity.md) of [Bugs](../B/bug.md)** : Evaluate the severity of the defects discovered. High-severity bugs can indicate the effectiveness of Ad Hoc testing in uncovering critical issues.
  - **[Test Coverage](../T/test-coverage.md)** : Although difficult to quantify in Ad Hoc testing, use code coverage tools post-testing to assess which areas of the application were inadvertently tested.
  - **Time to Discover** : Measure the time it takes to find defects. Ad Hoc testing might uncover certain bugs faster than structured testing.
  - **Cost of [Bugs](../B/bug.md)** : Analyze the cost savings from identifying and fixing bugs early, which can be attributed to the informal and rapid nature of Ad Hoc testing.
  - **Feedback from Testers** : Collect qualitative feedback from testers on the ease of finding defects and their perception of the thoroughness of Ad Hoc testing.

#### How can Ad Hoc testing be integrated into a continuous integration/continuous deployment (CI/CD) pipeline?

  Integrating **[Ad Hoc testing](../A/ad-hoc-testing.md)** into a CI/CD pipeline involves strategic, yet informal, testing efforts to complement the automated and structured tests. Since Ad Hoc is exploratory and often manual, it doesn't fit directly into automation pipelines. However, it can be incorporated as follows:

  - **Post-Deployment Sanity Checks**: After automated deployment, engineers can conduct Ad Hoc tests on the live system to quickly validate functionality and environment-specific issues.
  - **Scheduled Manual Test Sessions**: Reserve time slots within the CI/CD process for testers to perform [Ad Hoc testing](../A/ad-hoc-testing.md) on the latest build, ensuring immediate feedback on the most recent changes.
  - **Feedback Integration**: Use a feedback mechanism to report findings from [Ad Hoc testing](../A/ad-hoc-testing.md) back into the CI/CD pipeline. This could involve creating automated tickets or updating [test cases](../T/test-case.md).
  - **[Risk-Based Testing](../R/risk-based-testing.md) Triggers**: Implement a system where, based on code changes or areas with high risk, testers are alerted to perform targeted [Ad Hoc testing](../A/ad-hoc-testing.md).
  - **Exploratory [Test Tools](../T/test-tool.md)**: Utilize tools that support [exploratory testing](../E/exploratory-testing.md) within a CI/CD context, allowing for session-based [test management](../T/test-management.md) and reporting.
  - **Documentation and Tracking**: Ensure Ad Hoc findings are documented and tracked like other [test cases](../T/test-case.md), to inform future automated tests and improve regression suites.
  Remember, while [Ad Hoc testing](../A/ad-hoc-testing.md) can't be automated, its results can inform and enhance automated [test suites](../T/test-suite.md), making it a valuable asset in the continuous delivery ecosystem.

  - **Post-Deployment Sanity Checks**: After automated deployment, engineers can conduct Ad Hoc tests on the live system to quickly validate functionality and environment-specific issues.
  - **Scheduled Manual Test Sessions**: Reserve time slots within the CI/CD process for testers to perform [Ad Hoc testing](../A/ad-hoc-testing.md) on the latest build, ensuring immediate feedback on the most recent changes.
  - **Feedback Integration**: Use a feedback mechanism to report findings from [Ad Hoc testing](../A/ad-hoc-testing.md) back into the CI/CD pipeline. This could involve creating automated tickets or updating [test cases](../T/test-case.md).
  - **[Risk-Based Testing](../R/risk-based-testing.md) Triggers**: Implement a system where, based on code changes or areas with high risk, testers are alerted to perform targeted [Ad Hoc testing](../A/ad-hoc-testing.md).
  - **Exploratory [Test Tools](../T/test-tool.md)**: Utilize tools that support [exploratory testing](../E/exploratory-testing.md) within a CI/CD context, allowing for session-based [test management](../T/test-management.md) and reporting.
  - **Documentation and Tracking**: Ensure Ad Hoc findings are documented and tracked like other [test cases](../T/test-case.md), to inform future automated tests and improve regression suites.
