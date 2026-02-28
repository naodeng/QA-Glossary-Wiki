# Severity


<!-- TOC START -->
- [Questions about Severity ?](#questions-about-severity)
  - [Basics and Importance](#basics-and-importance)
    - [What is the definition of severity in software testing?](#what-is-the-definition-of-severity-in-software-testing)
    - [Why is understanding severity important in software testing?](#why-is-understanding-severity-important-in-software-testing)
    - [How does severity differ from priority in bug tracking?](#how-does-severity-differ-from-priority-in-bug-tracking)
  - [Severity Levels](#severity-levels)
    - [What are the different levels of severity in software testing?](#what-are-the-different-levels-of-severity-in-software-testing)
    - [How is the severity level of a bug determined?](#how-is-the-severity-level-of-a-bug-determined)
    - [What is the impact of high severity bugs on the software?](#what-is-the-impact-of-high-severity-bugs-on-the-software)
  - [Severity and Bug Life Cycle](#severity-and-bug-life-cycle)
    - [How does severity affect the bug life cycle?](#how-does-severity-affect-the-bug-life-cycle)
    - [What role does severity play in bug triage?](#what-role-does-severity-play-in-bug-triage)
    - [How does the severity of a bug influence its resolution time?](#how-does-the-severity-of-a-bug-influence-its-resolution-time)
  - [Severity in Different Testing Stages](#severity-in-different-testing-stages)
    - [How is severity considered in unit testing?](#how-is-severity-considered-in-unit-testing)
    - [How is severity considered in integration testing?](#how-is-severity-considered-in-integration-testing)
    - [How is severity considered in system testing?](#how-is-severity-considered-in-system-testing)
    - [How is severity considered in acceptance testing?](#how-is-severity-considered-in-acceptance-testing)
  - [Severity in Test Management](#severity-in-test-management)
    - [How does severity influence test case design?](#how-does-severity-influence-test-case-design)
    - [How does severity influence test execution planning?](#how-does-severity-influence-test-execution-planning)
    - [How does severity influence test reporting?](#how-does-severity-influence-test-reporting)
<!-- TOC END -->

Severity

gauges a defect's impact on an application's system. Defects with major system repercussions are assigned higher

severity

levels, typically determined by the

Quality Assurance

Engineer.

## Questions about Severity ?

### Basics and Importance

#### What is the definition of severity in software testing?

  In [software testing](../S/software-testing.md), **[severity](../S/severity.md)** refers to the impact a defect has on the operation of the software. It indicates the extent to which a [bug](../B/bug.md) can affect the system's functionality, performance, or stability. [Severity](../S/severity.md) is typically classified into categories such as **Critical**, **High**, **Medium**, and **Low**, reflecting the range from system crashes or data loss to minor issues that do not significantly impair user experience. Determining [severity](../S/severity.md) is a technical assessment and does not necessarily take into account the timeline or business priorities for fixing the issue. It is crucial for [test automation](../T/test-automation.md) engineers to accurately assess and assign [severity](../S/severity.md) to ensure that the most impactful defects are addressed promptly and to maintain the quality of the software product.

#### Why is understanding severity important in software testing?

  Understanding [severity](../S/severity.md) in [software testing](../S/software-testing.md) is crucial because it helps **allocate resources** effectively and **prioritize** testing and [bug](../B/bug.md)-fixing efforts. [Severity](../S/severity.md) indicates the impact a defect has on the system's operation, which directly influences the **risk** associated with the software release.
  When a [bug](../B/bug.md) is identified, knowing its [severity](../S/severity.md) allows test engineers to **communicate the potential consequences** to stakeholders, ensuring that the most critical issues are addressed first. This prioritization ensures that the software meets its **quality standards** and **[functional requirements](../F/functional-requirements.md)** before release.
  In addition, [severity](../S/severity.md) understanding aids in **risk management**. High-[severity](../S/severity.md) [bugs](../B/bug.md) might pose significant risks such as data loss, security breaches, or system crashes, which could have dire repercussions for the end-user and the company. By focusing on these [bugs](../B/bug.md), teams can mitigate risks and prevent costly post-release fixes or damage to the company's reputation.
  Moreover, [severity](../S/severity.md) plays a role in **test planning**. [Test cases](../T/test-case.md) that cover functionalities prone to high-[severity](../S/severity.md) issues may be executed earlier in the test cycle. This early detection allows for more time to resolve serious defects and manage their impact on the project timeline.
  Finally, [severity](../S/severity.md) assessment contributes to **continuous improvement** in the testing process. By analyzing the [severity](../S/severity.md) of past defects, teams can identify areas of the application that may require more robust testing or design improvements, leading to higher quality in future releases.

#### How does severity differ from priority in bug tracking?

  [Severity](../S/severity.md) and [priority](../P/priority.md) in [bug](../B/bug.md) tracking are distinct yet related concepts. **[Severity](../S/severity.md)** refers to the impact a [bug](../B/bug.md) has on the system's functionality, ranging from critical system crashes to minor UI issues. It's an objective measure of the [bug](../B/bug.md)'s technical impact.
  **[Priority](../P/priority.md)**, on the other hand, indicates the order in which a [bug](../B/bug.md) should be addressed, based on factors like business needs, customer impact, or release schedules. It's a subjective decision made by the team, often influenced by external stakeholders.
  While a high-[severity](../S/severity.md) [bug](../B/bug.md) typically commands high [priority](../P/priority.md), this isn't always the case. For example, a severe [bug](../B/bug.md) affecting a rarely used feature might be given a lower [priority](../P/priority.md) than a moderate [bug](../B/bug.md) in a critical component. Conversely, a low-[severity](../S/severity.md) cosmetic issue might be prioritized if it affects a key marketing feature.
  In essence, [severity](../S/severity.md) is about the [bug](../B/bug.md)'s technical effect, while [priority](../P/priority.md) is about the urgency of fixing it in the context of project goals. Both are crucial for effective [bug](../B/bug.md) management and ensuring a balanced approach to quality and delivery timelines.

### Severity Levels

#### What are the different levels of severity in software testing?

  [Severity](../S/severity.md) levels in [software testing](../S/software-testing.md) typically range from **Critical** to **Minor**:

  - **Critical**: The defect causes system failure or poses a significant threat to the system's security. It must be addressed immediately as it can affect business operations and data integrity.
  - **High**: The [bug](../B/bug.md) significantly impairs functionality, but there is a workaround. It should be resolved before product release.
  - **Medium**: This level indicates a problem that affects functionality but has less impact than a high [severity](../S/severity.md) issue. It should be fixed after high [severity](../S/severity.md) issues are resolved.
  - **Low**: The defect is an inconvenience, often related to UI or usability issues that do not affect the core functionality of the application.
  - **Minor**: These are trivial issues that do not need immediate attention and have the least impact on the functionality of the application.
  Each organization may have its own set of [severity](../S/severity.md) levels or definitions, but the above categories are commonly used in the industry. [Severity](../S/severity.md) levels guide the order in which [bugs](../B/bug.md) are addressed and help manage the testing and development efforts effectively.

  - **Critical**: The defect causes system failure or poses a significant threat to the system's security. It must be addressed immediately as it can affect business operations and data integrity.
  - **High**: The [bug](../B/bug.md) significantly impairs functionality, but there is a workaround. It should be resolved before product release.
  - **Medium**: This level indicates a problem that affects functionality but has less impact than a high [severity](../S/severity.md) issue. It should be fixed after high [severity](../S/severity.md) issues are resolved.
  - **Low**: The defect is an inconvenience, often related to UI or usability issues that do not affect the core functionality of the application.
  - **Minor**: These are trivial issues that do not need immediate attention and have the least impact on the functionality of the application.

#### How is the severity level of a bug determined?

  The [severity](../S/severity.md) level of a [bug](../B/bug.md) is determined by assessing its **impact on the system's functionality**, **user experience**, and **business operations**. To evaluate [severity](../S/severity.md), consider the following factors:

  - **Functionality Impact** : How does the bug affect application features?
    Does it cause a complete breakdown, partial malfunction, or minor inconvenience?

  - **Data Impact** : Does the bug lead to data loss, corruption, or compromise data integrity?
  - **Frequency** : How often does the bug occur?
    Is it easily reproducible or a rare event?

  - **Scope** : Is the issue localized to a specific module, or does it have widespread effects across the application?
  - **User Impact** : How does the bug affect the end-user?
    Consider both direct effects on usability and indirect effects on user perception and satisfaction.

  - **Workaround Availability** : Can users bypass the issue through alternative means, or is the bug blocking critical functionality without a workaround?
  - **Legal and Compliance** : Does the bug cause non-compliance with regulatory requirements or contractual obligations?
  After considering these factors, a [bug](../B/bug.md) is typically classified into categories such as **Critical**, **High**, **Medium**, or **Low** [severity](../S/severity.md). The classification is often a collaborative decision involving testers, developers, and product managers, ensuring a balanced perspective on the [bug](../B/bug.md)'s impact. This assessment guides prioritization and resolution efforts, ensuring that the most detrimental issues are addressed promptly.

  - **Functionality Impact** : How does the bug affect application features?
    Does it cause a complete breakdown, partial malfunction, or minor inconvenience?

  - **Data Impact** : Does the bug lead to data loss, corruption, or compromise data integrity?
  - **Frequency** : How often does the bug occur?
    Is it easily reproducible or a rare event?

  - **Scope** : Is the issue localized to a specific module, or does it have widespread effects across the application?
  - **User Impact** : How does the bug affect the end-user?
    Consider both direct effects on usability and indirect effects on user perception and satisfaction.

  - **Workaround Availability** : Can users bypass the issue through alternative means, or is the bug blocking critical functionality without a workaround?
  - **Legal and Compliance** : Does the bug cause non-compliance with regulatory requirements or contractual obligations?

#### What is the impact of high severity bugs on the software?

  High [severity](../S/severity.md) [bugs](../B/bug.md) have a significant impact on software as they typically indicate critical issues that can lead to system crashes, data loss, or security vulnerabilities. These [bugs](../B/bug.md) often:

  - **Block**
    major functionalities, preventing users from performing essential operations.

  - **Necessitate immediate attention**
    and resources, potentially disrupting the development workflow and causing re-prioritization of tasks.

  - **Increase the risk**
    of missing release deadlines if they are found late in the development cycle.

  - **Affect customer trust**
    and satisfaction if they make it into production, especially if they compromise data integrity or privacy.

  - **Require extensive testing**
    post-fix to ensure that the issue is resolved without introducing new problems, which can further delay the release.
  In [test automation](../T/test-automation.md), high [severity](../S/severity.md) [bugs](../B/bug.md) may lead to:

  - **Re-evaluation of [test coverage](../T/test-coverage.md)**
    to understand why the bug was not caught earlier.

  - **Adjustments in test strategies**
    to include more rigorous checks around critical areas.

  - **Increased maintenance**
    of test scripts if the bugs lead to significant changes in the application's codebase.
  Overall, high [severity](../S/severity.md) [bugs](../B/bug.md) demand a swift and thorough response to maintain [software quality](../S/software-quality.md) and project timelines.

  - **Block**
    major functionalities, preventing users from performing essential operations.

  - **Necessitate immediate attention**
    and resources, potentially disrupting the development workflow and causing re-prioritization of tasks.

  - **Increase the risk**
    of missing release deadlines if they are found late in the development cycle.

  - **Affect customer trust**
    and satisfaction if they make it into production, especially if they compromise data integrity or privacy.

  - **Require extensive testing**
    post-fix to ensure that the issue is resolved without introducing new problems, which can further delay the release.

  - **Re-evaluation of [test coverage](../T/test-coverage.md)**
    to understand why the bug was not caught earlier.

  - **Adjustments in test strategies**
    to include more rigorous checks around critical areas.

  - **Increased maintenance**
    of test scripts if the bugs lead to significant changes in the application's codebase.

### Severity and Bug Life Cycle

#### How does severity affect the bug life cycle?

  [Severity](../S/severity.md) affects the [bug](../B/bug.md) life cycle by influencing the **order** and **urgency** with which [bugs](../B/bug.md) are addressed during the development and testing phases. High-[severity](../S/severity.md) [bugs](../B/bug.md) often lead to a **halt in the release process** until they are resolved, due to their potential to cause significant harm to the system or the end-user experience. These [bugs](../B/bug.md) are typically **escalated** to the top of the development team's priorities.
  In contrast, lower-[severity](../S/severity.md) [bugs](../B/bug.md) may be scheduled for fixing in later releases or might be bundled with other minor fixes. The **workflow** and **resource allocation** for fixing [bugs](../B/bug.md) are often directly tied to their [severity](../S/severity.md); critical [bugs](../B/bug.md) might require immediate attention from senior developers or lead to **overtime work**, while minor ones could be assigned to less experienced team members or addressed during normal development cycles.
  Moreover, [severity](../S/severity.md) can affect the **communication** with stakeholders. High-[severity](../S/severity.md) issues usually warrant immediate notification and detailed reporting to both internal teams and potentially external stakeholders, depending on the nature of the [bug](../B/bug.md) and the business context.
  In [automated testing](../A/automated-testing.md) environments, [severity](../S/severity.md) can also influence the **automation strategy**. Tests that cover critical areas of the application might be run more frequently or with higher [priority](../P/priority.md) in continuous integration pipelines to ensure that high-[severity](../S/severity.md) [bugs](../B/bug.md) are caught and addressed as early as possible.
  Overall, [severity](../S/severity.md) is a key factor in **decision-making processes** related to [bug](../B/bug.md) fixes, affecting everything from prioritization and resource management to stakeholder communication and testing strategies.

#### What role does severity play in bug triage?

  In [bug](../B/bug.md) triage, **[severity](../S/severity.md)** plays a critical role in decision-making processes regarding the **allocation of resources** and the **order of [bug](../B/bug.md) fixes**. It helps in assessing the **impact of a [bug](../B/bug.md)** on the application's functionality and the user experience. During triage meetings, the team evaluates the [severity](../S/severity.md) to understand the **urgency** and **scope** of the problem.
  High-[severity](../S/severity.md) [bugs](../B/bug.md) often require **immediate attention** and can lead to a **re-prioritization** of the development and testing efforts. They may also trigger a **reassessment** of the release schedule if they pose significant risks to the product's stability or security. Conversely, lower-[severity](../S/severity.md) [bugs](../B/bug.md) might be scheduled for later sprints or releases, allowing the team to focus on more critical issues first.
  The [severity](../S/severity.md) assessment influences the **communication** with stakeholders, as high-[severity](../S/severity.md) issues may warrant immediate notifications and detailed reports. It also guides the **risk management strategy**, ensuring that the most damaging [bugs](../B/bug.md) are addressed promptly to minimize their impact on the end product.
  In [automated testing](../A/automated-testing.md) scenarios, [severity](../S/severity.md) can dictate the **automation strategy**, such as prioritizing the creation of automated tests for critical areas of the application to quickly identify and address high-[severity](../S/severity.md) [bugs](../B/bug.md) in future development cycles.
  Ultimately, understanding and accurately assessing [bug](../B/bug.md) [severity](../S/severity.md) during triage ensures that the team can maintain a **balanced workload**, **optimize the [quality assurance](../Q/quality-assurance.md) process**, and deliver a **reliable software product** within the desired timeframe.

#### How does the severity of a bug influence its resolution time?

  The **[severity](../S/severity.md)** of a [bug](../B/bug.md) typically dictates the urgency of its resolution. High-[severity](../S/severity.md) [bugs](../B/bug.md), such as those causing data loss, security breaches, or system crashes, are often addressed **immediately** due to their potential to critically impact the application's functionality or user experience. These [bugs](../B/bug.md) can halt production or release processes until resolved.
  Conversely, lower-[severity](../S/severity.md) [bugs](../B/bug.md), like minor UI issues or spelling errors, may be scheduled for resolution in future releases or during less critical maintenance windows. Their resolution time is generally longer as they do not impede core functionalities and are often considered **tolerable** in the short term.
  The resolution time is also influenced by the **complexity** of the [bug](../B/bug.md) and the **availability** of resources. Even a high-[severity](../S/severity.md) [bug](../B/bug.md) may take longer to resolve if it requires significant investigation or if it is deeply entrenched in the system architecture. Additionally, if key personnel or necessary resources are not available, the resolution may be delayed despite the [severity](../S/severity.md).
  In practice, resolution time is a balance between the [severity](../S/severity.md) of the [bug](../B/bug.md) and the **practicalities** of the development process. While [severity](../S/severity.md) pushes for a quicker response, other factors such as resource allocation, sprint planning, and the presence of workarounds can adjust the actual time taken to address the issue.

### Severity in Different Testing Stages

#### How is severity considered in unit testing?

  In **[unit testing](../U/unit-testing.md)**, [severity](../S/severity.md) is typically less emphasized compared to other testing stages, as the focus is on verifying the smallest testable parts of the application in isolation. However, when a defect is identified at the unit level, its [severity](../S/severity.md) can still be considered in terms of its impact on the functionality of the unit under test.
  If a unit test fails, it indicates a defect that could range from a minor discrepancy in the expected output to a critical failure that prevents the unit from performing its intended function. The [severity](../S/severity.md) in this context is often implicitly high, as unit tests aim to ensure the correctness of individual functions or methods, which are fundamental building blocks of the application.
  Automated unit tests are designed to run frequently and provide quick feedback, so any failure is typically addressed **immediately** by developers before the code is integrated into the larger system. This immediate action reduces the need for a detailed [severity](../S/severity.md) classification at the [unit testing](../U/unit-testing.md) level.
  However, in some cases, if a unit test failure is due to a non-critical aspect that does not impede the overall functionality or if it's a known issue that's been deprioritized, the [severity](../S/severity.md) might be considered lower, and the fix might be deferred. This decision is usually made in the context of the project's priorities and timelines.
  In summary, while [severity](../S/severity.md) is a crucial concept in later stages of testing, in [unit testing](../U/unit-testing.md), any defect that causes a test to fail is often treated with urgency, reflecting an implicit high [severity](../S/severity.md) due to the foundational nature of unit-level code.

#### How is severity considered in integration testing?

  In [integration testing](../I/integration-testing.md), **[severity](../S/severity.md)** is a critical factor when identifying, assessing, and resolving defects that arise from the interaction between integrated components or systems. Unlike [unit testing](../U/unit-testing.md), which focuses on individual units of code, [integration testing](../I/integration-testing.md) evaluates the collective operation, where defects often have broader implications.
  [Severity](../S/severity.md) in this context helps to gauge the impact of a defect on the system's functionality, stability, and performance. High-[severity](../S/severity.md) issues, such as those causing system crashes or data corruption, are typically addressed before lower-[severity](../S/severity.md) issues, like minor UI discrepancies that do not affect overall operation.
  [Test automation](../T/test-automation.md) engineers use [severity](../S/severity.md) to prioritize defect fixes, especially when time constraints or resources are limited. Automated [test suites](../T/test-suite.md) may be designed to flag high-[severity](../S/severity.md) defects immediately, triggering alerts for rapid investigation. This ensures that the most critical issues are addressed promptly, reducing the risk of significant faults slipping through to later stages of testing or production.
  When planning [test execution](../T/test-execution.md), tests covering critical integration paths may be run more frequently or with higher [priority](../P/priority.md), especially if they have previously uncovered high-[severity](../S/severity.md) defects. In test reporting, [severity](../S/severity.md) provides a clear metric for communicating the health of the system to stakeholders, influencing decisions on release readiness and resource allocation.
  In summary, [severity](../S/severity.md) in [integration testing](../I/integration-testing.md) is a key metric for prioritizing defect resolution, informing test planning, and communicating risk to ensure that the most impactful issues are addressed efficiently and effectively.

#### How is severity considered in system testing?

  In [system testing](../S/system-testing.md), **[severity](../S/severity.md)** is a critical factor when deciding the order in which [bugs](../B/bug.md) are addressed and the level of attention they require. It is considered alongside other factors such as [priority](../P/priority.md), but it specifically refers to the impact a defect has on the system's operation.
  [Severity](../S/severity.md) is used to assess the extent to which a [bug](../B/bug.md) can **affect the system's functionality, performance, or stability**. High [severity](../S/severity.md) issues, such as those causing system crashes or data loss, are typically addressed before lower [severity](../S/severity.md) issues, like minor UI glitches that do not impede core functionalities.
  During [system testing](../S/system-testing.md), [test cases](../T/test-case.md) may be weighted or ordered based on the potential [severity](../S/severity.md) of the defects they are designed to uncover. [Test automation](../T/test-automation.md) engineers use [severity](../S/severity.md) to prioritize which automated tests to run and when, especially when time or resources are limited. For example, tests covering critical system components may be run more frequently or ahead of others.
  When a high [severity](../S/severity.md) defect is found, it can trigger a **focused testing effort** on the affected area to ensure that related functionalities are not compromised. This can involve additional automated regression tests or targeted [exploratory testing](../E/exploratory-testing.md).
  In test reporting, [severity](../S/severity.md) is a key metric. It helps stakeholders understand the health of the system and make informed decisions about release readiness. Reports often include [severity](../S/severity.md) distribution to highlight the seriousness of outstanding defects, influencing go/no-go decisions.

#### How is severity considered in acceptance testing?

  In [acceptance testing](../A/acceptance-testing.md), **[severity](../S/severity.md)** is a critical factor when evaluating whether a software product meets the specified acceptance criteria. It guides the decision-making process regarding the product's readiness for release. High-[severity](../S/severity.md) issues often indicate fundamental problems that could **jeopardize the user experience** or cause **system failure**, thus must be addressed before the product can be accepted.
  Acceptance tests are designed to mimic real-world usage and ensure that the product is capable of performing its intended functions in a live environment. When a [bug](../B/bug.md) is encountered, its [severity](../S/severity.md) reflects the extent to which it disrupts these critical functions. [Bugs](../B/bug.md) with **severe impact on functionality, security, or performance** are typically considered blockers and must be resolved before acceptance is granted.
  During [acceptance testing](../A/acceptance-testing.md), automation engineers focus on:

  - **Identifying**
    and
    **documenting**
    severe bugs that could impede the user's ability to operate the software effectively.

  - **Assessing**
    the severity to determine if it falls within an acceptable risk threshold for the release.

  - **Prioritizing**
    the resolution of severe bugs to ensure a stable and functional product at launch.
  The [severity](../S/severity.md) assessment in [acceptance testing](../A/acceptance-testing.md) is not just about identifying defects but also about ensuring that the product delivers a **quality user experience** and meets the **business requirements**. Any severe issues identified must be communicated to stakeholders promptly to make informed decisions about the product's release readiness.

  - **Identifying**
    and
    **documenting**
    severe bugs that could impede the user's ability to operate the software effectively.

  - **Assessing**
    the severity to determine if it falls within an acceptable risk threshold for the release.

  - **Prioritizing**
    the resolution of severe bugs to ensure a stable and functional product at launch.

### Severity in Test Management

#### How does severity influence test case design?

  [Severity](../S/severity.md) influences [test case](../T/test-case.md) design by dictating the **focus** and **depth** of testing efforts. High-[severity](../S/severity.md) areas often require **robust** [test cases](../T/test-case.md) that cover a wide range of scenarios, including edge cases and stress conditions. [Test cases](../T/test-case.md) for these areas are designed with **thoroughness** in mind, often employing **[negative testing](../N/negative-testing.md)** techniques to ensure the system can handle invalid inputs or unexpected user behaviors.
  For example, if a feature is related to security or data integrity, its failure would be considered high [severity](../S/severity.md). [Test cases](../T/test-case.md) for such features would include:

  ```
  // Pseudocode for a high-severity test case
  test('Sensitive data encryption', () => {
    const sensitiveData = 'user_password';
    const encryptedData = encrypt(sensitiveData);
    expect(encryptedData).not.toBe(sensitiveData);
    expect(isEncrypted(encryptedData)).toBe(true);
  });
  ```
  In contrast, lower-[severity](../S/severity.md) areas might be tested with more **straightforward** and **simpler** [test cases](../T/test-case.md), focusing on the most common and expected [use cases](../U/use-case.md). These [test cases](../T/test-case.md) might not delve as deeply into rare scenarios or stress conditions, as the impact of failure is less critical.
  [Test case](../T/test-case.md) design also considers the **likelihood** of a [bug](../B/bug.md) occurring in conjunction with [severity](../S/severity.md). High-[severity](../S/severity.md) areas with a high likelihood of failure may have **additional [test cases](../T/test-case.md)** or **automated checks** to catch potential regressions quickly.
  Ultimately, [severity](../S/severity.md) guides the **allocation of resources** and **time** in [test case](../T/test-case.md) design, ensuring that the most critical aspects of the software are thoroughly tested and reliable.

#### How does severity influence test execution planning?

  [Severity](../S/severity.md) influences [test execution](../T/test-execution.md) planning by dictating the **order** and **[priority](../P/priority.md)** in which [test cases](../T/test-case.md) are executed. High-[severity](../S/severity.md) issues, which could cause significant functionality breakdowns or data loss, are tested first to ensure the most critical aspects of the software are stable. This approach helps in identifying and addressing the most damaging defects early in the test cycle.
  [Test cases](../T/test-case.md) that cover areas of the application with known high-[severity](../S/severity.md) issues may be **prioritized** and executed more frequently, such as in [regression testing](../R/regression-testing.md), to confirm that these issues have been resolved and have not reappeared. Conversely, areas with lower-[severity](../S/severity.md) issues might be tested less frequently or with less urgency.
  In [automated testing](../A/automated-testing.md), [test suites](../T/test-suite.md) can be organized to run high-[severity](../S/severity.md) [test cases](../T/test-case.md) as part of a **smoke test** or a **sanity test** suite to quickly assess the health of a build. This ensures that any build or release candidate meets the minimum criteria for further testing or deployment.
  Moreover, when planning [test execution](../T/test-execution.md), it's crucial to allocate appropriate **resources** and **time** to high-[severity](../S/severity.md) [test scenarios](../T/test-scenario.md). This might involve setting up more robust testing environments or dedicating more time for [test execution](../T/test-execution.md) and analysis.
  In summary, [severity](../S/severity.md) guides the focus of [test execution](../T/test-execution.md) towards the most critical areas of the application, ensuring that the most impactful issues are addressed promptly, thereby optimizing the testing effort and contributing to the overall quality of the software.

#### How does severity influence test reporting?

  [Severity](../S/severity.md) influences test reporting by guiding the **communication** and **management** of defects. When reporting test results, [severity](../S/severity.md) provides a clear indication of the **impact** a [bug](../B/bug.md) has on the system's functionality. [Test reports](../T/test-report.md) typically include a **[severity](../S/severity.md) rating** for each defect to help stakeholders understand the potential risk and urgency for fixes.
  In automated test reporting, [severity](../S/severity.md) ratings can trigger **alerts** and **notifications** to the appropriate team members. For instance, a high-[severity](../S/severity.md) [bug](../B/bug.md) might automatically notify a product manager or lead developer, prompting immediate action. This ensures that critical issues are addressed promptly, reducing the risk of significant problems at release.
  Moreover, [severity](../S/severity.md) can influence the **ordering** of reported defects. [Test reports](../T/test-report.md) might be sorted to present the most severe [bugs](../B/bug.md) at the top, ensuring they receive attention first. This helps prioritize defect resolution efforts according to the potential impact on the product.
  Additionally, [severity](../S/severity.md) ratings in [test reports](../T/test-report.md) can be used to generate **metrics** and **trends** over time, providing insights into the quality of the software. High-[severity](../S/severity.md) [bugs](../B/bug.md) trending downwards could indicate an improvement in [software quality](../S/software-quality.md), while an upward trend might signal a need for process or design changes.
  In summary, [severity](../S/severity.md) in test reporting:

  - Communicates the impact of defects.
  - Triggers alerts for immediate action.
  - Prioritizes bugs in the report.
  - Generates quality metrics and trends.
  By effectively utilizing [severity](../S/severity.md) in test reporting, teams can ensure that critical issues are highlighted and addressed, maintaining focus on delivering high-quality software.

  - Communicates the impact of defects.
  - Triggers alerts for immediate action.
  - Prioritizes bugs in the report.
  - Generates quality metrics and trends.
