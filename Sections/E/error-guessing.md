# Error Guessing

<!-- TOC START -->
- [Related Terms:](#related-terms)
  - [See also:](#see-also)
- [Questions about Error Guessing ?](#questions-about-error-guessing)
  - [Basics and Importance](#basics-and-importance)
    - [What is error guessing in software testing?](#what-is-error-guessing-in-software-testing)
    - [Why is error guessing considered an important technique in software testing?](#why-is-error-guessing-considered-an-important-technique-in-software-testing)
    - [What is the difference between error guessing and other testing techniques?](#what-is-the-difference-between-error-guessing-and-other-testing-techniques)
    - [What are the advantages and disadvantages of error guessing?](#what-are-the-advantages-and-disadvantages-of-error-guessing)
  - [Techniques and Strategies](#techniques-and-strategies)
    - [What strategies are commonly used in error guessing?](#what-strategies-are-commonly-used-in-error-guessing)
    - [How can a tester develop their error guessing skills?](#how-can-a-tester-develop-their-error-guessing-skills)
    - [What is the role of experience in error guessing?](#what-is-the-role-of-experience-in-error-guessing)
    - [How can error guessing be combined with other testing techniques?](#how-can-error-guessing-be-combined-with-other-testing-techniques)
  - [Practical Application](#practical-application)
    - [Can you provide examples of situations where error guessing would be particularly useful?](#can-you-provide-examples-of-situations-where-error-guessing-would-be-particularly-useful)
    - [How can error guessing be applied in automated testing?](#how-can-error-guessing-be-applied-in-automated-testing)
    - [What types of errors are typically identified using error guessing?](#what-types-of-errors-are-typically-identified-using-error-guessing)
    - [How can the effectiveness of error guessing be measured?](#how-can-the-effectiveness-of-error-guessing-be-measured)
<!-- TOC END -->

Error Guessing

is a

software testing

technique where the tester, relying on their experience, intuition, and knowledge of the system, tries to predict where defects might occur. Instead of following a systematic testing approach or predefined

test cases

, testers make educated guesses to identify potential problem areas or scenarios where the software might fail. The technique is based on the tester's familiarity with common errors, past defects, or specific system behavior.

Error guessing

is often used as a supplementary testing method, complementing more structured techniques, and is particularly effective in identifying unique or unanticipated issues.

## Related Terms:

- [Heuristic Testing](https://naodeng.com.cn/en/wiki/heuristic-testing)

### See also:

- [Wikipedia](https://en.wikipedia.org/wiki/Error_guessing)

## Questions about Error Guessing ?

### Basics and Importance

#### What is error guessing in software testing?

  [Error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is a **[test case](https://naodeng.com.cn/en/wiki/test-case) design technique** where testers use their intuition, experience, and understanding of the system to predict where [bugs](https://naodeng.com.cn/en/wiki/bug) might occur, without following any formal methodology. Testers leverage their knowledge of common pitfalls and specific system quirks to identify potential error conditions.
  In practice, [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) involves creating tests based on **hunches** or **past experiences** with similar applications. Testers might consider factors like boundary conditions, invalid inputs, and complex user scenarios that are likely to cause errors.
  To enhance [error guessing](https://naodeng.com.cn/en/wiki/error-guessing), testers can keep a **repository of common [bugs](https://naodeng.com.cn/en/wiki/bug)** and use **checklists** derived from historical defect data. Regularly reviewing past defects and learning from them can sharpen a tester's intuition.
  In [automated testing](https://naodeng.com.cn/en/wiki/automated-testing), [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) can inform the creation of **[test scripts](https://naodeng.com.cn/en/wiki/test-script)** that target likely failure points. For example, if a tester suspects that a form might not handle special characters properly, they might write an automated test that inputs those characters into the form fields.
  While [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is less structured than other techniques, it can be **complementary**. It often fills in gaps left by more formal methods, providing a safety net that catches issues that might otherwise be missed.
  To gauge its effectiveness, teams can track the **number of defects found** through [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) compared to other methods. If [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) consistently uncovers significant issues, it validates the technique's value within the testing strategy.

#### Why is error guessing considered an important technique in software testing?

  [Error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is crucial in [software testing](https://naodeng.com.cn/en/wiki/software-testing) because it leverages the **tester's intuition and experience** to anticipate and simulate unconventional or edge-case scenarios that may not be covered by formal testing techniques. It acts as a **complement to systematic methods**, filling in the gaps that structured approaches might miss. Testers apply their understanding of common failures and domain knowledge to hypothesize potential error conditions.
  This technique is particularly valuable because it can **identify unique and unanticipated [bugs](https://naodeng.com.cn/en/wiki/bug)**. While structured tests are based on specifications and predefined criteria, [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is dynamic and can adapt to the evolving understanding of the application and its environment.
  Incorporating [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) into [test automation](https://naodeng.com.cn/en/wiki/test-automation) involves creating scripts based on the **tester's hypotheses** about potential errors. These scripts can be run alongside regular automated tests to catch issues that might otherwise slip through.
  To enhance [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) effectiveness, testers should **continuously learn from past defects**, stay updated with common issues in similar applications, and share knowledge with peers. Metrics like defect detection rate can help measure its impact.
  In summary, [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is a **vital technique** that adds a layer of human insight to the testing process, making it more robust and comprehensive. It is most effective when used in conjunction with other testing methods, ensuring a thorough exploration of the application's potential weaknesses.

#### What is the difference between error guessing and other testing techniques?

  [Error guessing](https://naodeng.com.cn/en/wiki/error-guessing) differs from other testing techniques primarily in its **lack of formal structure** and reliance on the tester's intuition and experience. While methods like **boundary value analysis** or **[equivalence partitioning](https://naodeng.com.cn/en/wiki/equivalence-partitioning)** are systematic and based on specific rules or models, [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is more **ad-hoc** and **heuristic-based**. It doesn't follow a predefined set of [test cases](https://naodeng.com.cn/en/wiki/test-case) but rather relies on the tester's ability to anticipate likely error sources.
  Other techniques often require detailed documentation and can be **easily automated** or **outsourced**. In contrast, [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is highly **subjective** and **personal**, making it harder to automate or transfer between testers without loss of effectiveness.
  Formal methods like **model-based testing** generate [test cases](https://naodeng.com.cn/en/wiki/test-case) from formal specifications, ensuring coverage of all defined scenarios. [Error guessing](https://naodeng.com.cn/en/wiki/error-guessing), however, targets areas that might be overlooked by formal methods, often based on past experiences with similar applications or common failure patterns.
  While structured methods can be more **comprehensive** and **repeatable**, [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) can quickly identify critical issues without the need for extensive preparation. It's typically used as a **complementary approach**, filling in the gaps left by more systematic techniques.
  In summary, [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is a **flexible**, **experience-driven** approach that contrasts with the **rigorous**, **rule-based** nature of other testing techniques. It's particularly useful for identifying unusual or overlooked errors that might not be caught by more formal methods.

#### What are the advantages and disadvantages of error guessing?

  Advantages of [Error Guessing](https://naodeng.com.cn/en/wiki/error-guessing):

  - **Intuitive** : Leverages tester's intuition and experience to identify potential weak spots.
  - **Flexible** : Adapts to different contexts and applications without the need for formal procedures.
  - **Efficient** : Quickly targets areas that are likely to fail, saving time in the testing process.
  - **Complementary** : Enhances structured testing methods by addressing cases that predefined tests might miss.
  Disadvantages of [Error Guessing](https://naodeng.com.cn/en/wiki/error-guessing):

  - **Subjective** : Relies heavily on individual skill and experience, leading to variability in results.
  - **Non-reproducible** : Lacks a formal methodology, making it difficult to replicate tests or share techniques across teams.
  - **Incomplete** : May not cover all possible error scenarios, especially in complex systems.
  - **Unpredictable** : Effectiveness is hard to measure and can lead to a false sense of security if key errors are overlooked.
  - **Intuitive** : Leverages tester's intuition and experience to identify potential weak spots.
  - **Flexible** : Adapts to different contexts and applications without the need for formal procedures.
  - **Efficient** : Quickly targets areas that are likely to fail, saving time in the testing process.
  - **Complementary** : Enhances structured testing methods by addressing cases that predefined tests might miss.
  - **Subjective** : Relies heavily on individual skill and experience, leading to variability in results.
  - **Non-reproducible** : Lacks a formal methodology, making it difficult to replicate tests or share techniques across teams.
  - **Incomplete** : May not cover all possible error scenarios, especially in complex systems.
  - **Unpredictable** : Effectiveness is hard to measure and can lead to a false sense of security if key errors are overlooked.

### Techniques and Strategies

#### What strategies are commonly used in error guessing?

  [Error guessing](https://naodeng.com.cn/en/wiki/error-guessing) strategies often hinge on the tester's intuition and experience. Common strategies include:

  - **Boundary Value Analysis** : Guessing errors at the edges of input ranges.
  - **[Stress Testing](https://naodeng.com.cn/en/wiki/stress-testing)** : Anticipating failures under high load or extreme conditions.
  - **Invalid Input** : Trying inputs that are outside of valid ranges or formats.
  - **Resource Depletion** : Guessing errors when system resources are low or exhausted.
  - **State Transition Errors** : Predicting failures when the system moves from one state to another.
  - **Interactions with External Systems** : Guessing errors that might occur during interactions with databases, APIs, or other services.
  - **Concurrency Issues** : Looking for race conditions and deadlocks in multi-threaded applications.
  - **User Behavior** : Simulating unusual or unexpected user actions.
  Incorporate these strategies into automated tests by scripting scenarios that reflect these guesses. For example:

  ```
  // Boundary Value Analysis Example
  test('should handle maximum input length', () => {
    const input = 'a'.repeat(MAX_INPUT_LENGTH);
    expect(() => processInput(input)).not.toThrow();
  });
  ```
  To measure effectiveness, track the number of defects found using [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) against those found by other methods. Adjust strategies based on defect trends and past experiences. Remember, [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is complementary to systematic techniques and should be used as part of a balanced testing approach.

  - **Boundary Value Analysis** : Guessing errors at the edges of input ranges.
  - **[Stress Testing](https://naodeng.com.cn/en/wiki/stress-testing)** : Anticipating failures under high load or extreme conditions.
  - **Invalid Input** : Trying inputs that are outside of valid ranges or formats.
  - **Resource Depletion** : Guessing errors when system resources are low or exhausted.
  - **State Transition Errors** : Predicting failures when the system moves from one state to another.
  - **Interactions with External Systems** : Guessing errors that might occur during interactions with databases, APIs, or other services.
  - **Concurrency Issues** : Looking for race conditions and deadlocks in multi-threaded applications.
  - **User Behavior** : Simulating unusual or unexpected user actions.

#### How can a tester develop their error guessing skills?

  To develop [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) skills, testers should:

  - **Practice regularly** : Engage in diverse testing scenarios to encounter a variety of bugs.
  - **Learn from past defects** : Analyze historical bug data to identify patterns and common failure points.
  - **Study the application domain** : Gain deep understanding of the software's domain to predict complex user behaviors and potential errors.
  - **Collaborate with others** : Share knowledge with peers to learn from their insights and experiences.
  - **Use checklists** : Create and refine checklists based on known error types to systematically guess potential errors.
  - **Stay updated** : Keep abreast of new technologies, tools, and testing methodologies to anticipate modern error types.
  - **Think like an end-user** : Adopt the user's perspective to uncover errors that may occur in real-world usage.
  - **Experiment** : Try unconventional test cases and scenarios to uncover less obvious errors.
  - **Review code changes** : Understand recent code modifications to target areas that might introduce new errors.
  By honing these skills, testers can improve their intuition and become more proficient in [error guessing](https://naodeng.com.cn/en/wiki/error-guessing), leading to more effective and efficient [test automation](https://naodeng.com.cn/en/wiki/test-automation).

  - **Practice regularly** : Engage in diverse testing scenarios to encounter a variety of bugs.
  - **Learn from past defects** : Analyze historical bug data to identify patterns and common failure points.
  - **Study the application domain** : Gain deep understanding of the software's domain to predict complex user behaviors and potential errors.
  - **Collaborate with others** : Share knowledge with peers to learn from their insights and experiences.
  - **Use checklists** : Create and refine checklists based on known error types to systematically guess potential errors.
  - **Stay updated** : Keep abreast of new technologies, tools, and testing methodologies to anticipate modern error types.
  - **Think like an end-user** : Adopt the user's perspective to uncover errors that may occur in real-world usage.
  - **Experiment** : Try unconventional test cases and scenarios to uncover less obvious errors.
  - **Review code changes** : Understand recent code modifications to target areas that might introduce new errors.

#### What is the role of experience in error guessing?

  Experience plays a crucial role in **[error guessing](https://naodeng.com.cn/en/wiki/error-guessing)** as it relies heavily on the tester's intuition and knowledge to anticipate where defects might occur. Experienced testers draw from their understanding of common failure patterns, past [bugs](https://naodeng.com.cn/en/wiki/bug), system behavior, and domain knowledge to make educated guesses about potential errors.
  With experience, testers develop an **intuitive sense** of 'smell' for code and system anomalies. They can often predict errors in areas such as boundary conditions, data flow, complex algorithms, and integrations based on their previous encounters with similar issues.
  Moreover, experienced testers are adept at recognizing **subtle clues** that may indicate deeper problems, such as inconsistent behavior or performance issues, which might not be immediately apparent to less experienced testers.
  To enhance [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) effectiveness, testers should continuously **reflect on past testing experiences**, analyze defects, and keep abreast of common issues reported in similar applications or technologies. This retrospective analysis helps in building a **mental repository** of potential problem areas that can be applied to future testing scenarios.
  In summary, the role of experience in [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is to leverage past insights and knowledge to **predict and identify errors** that might not be caught by more formalized testing techniques. It enriches the testing process by adding a layer of **human judgment** and **heuristic analysis** to the identification of potential defects.

#### How can error guessing be combined with other testing techniques?

  [Error guessing](https://naodeng.com.cn/en/wiki/error-guessing) can be effectively combined with other testing techniques to enhance the overall testing process. Here's how:

  - **Boundary Value Analysis (BVA)** : Use error guessing to identify potential off-by-one errors and other edge cases not covered by BVA.
  - **[Equivalence Partitioning](https://naodeng.com.cn/en/wiki/equivalence-partitioning)** : After partitioning input data, apply error guessing to hypothesize errors in each partition, especially those that seem more prone to issues.
  - **[Decision Table Testing](https://naodeng.com.cn/en/wiki/decision-table-testing)** : Incorporate error guessing to explore conditions and actions not represented in the decision table.
  - **[State Transition Testing](https://naodeng.com.cn/en/wiki/state-transition-testing)** : Use error guessing to predict illegal state transitions or unexpected behaviors in state machines.
  - **[Exploratory Testing](https://naodeng.com.cn/en/wiki/exploratory-testing)** : While performing exploratory testing, leverage error guessing to direct the exploration towards areas with suspected high risk.
  - **Automated [Regression Testing](https://naodeng.com.cn/en/wiki/regression-testing)** : Integrate error guesses as additional test cases to catch regressions in areas known to be fragile.
  In [automated testing](https://naodeng.com.cn/en/wiki/automated-testing), error guesses can be translated into specific [test cases](https://naodeng.com.cn/en/wiki/test-case) or assertions. For example:

  ```
  // Hypothetical error guess: Negative quantity leads to incorrect inventory count
  test('Inventory count should not decrease on negative quantity input', () => {
    const initialCount = getInventoryCount();
    addInventory(-5);
    expect(getInventoryCount()).toEqual(initialCount);
  });
  ```
  To measure the effectiveness of [error guessing](https://naodeng.com.cn/en/wiki/error-guessing), track the number of defects found using this technique versus total defects found. Additionally, analyze the [severity](https://naodeng.com.cn/en/wiki/severity) and impact of the defects caught by [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) to assess its value in the testing strategy.

  - **Boundary Value Analysis (BVA)** : Use error guessing to identify potential off-by-one errors and other edge cases not covered by BVA.
  - **[Equivalence Partitioning](https://naodeng.com.cn/en/wiki/equivalence-partitioning)** : After partitioning input data, apply error guessing to hypothesize errors in each partition, especially those that seem more prone to issues.
  - **[Decision Table Testing](https://naodeng.com.cn/en/wiki/decision-table-testing)** : Incorporate error guessing to explore conditions and actions not represented in the decision table.
  - **[State Transition Testing](https://naodeng.com.cn/en/wiki/state-transition-testing)** : Use error guessing to predict illegal state transitions or unexpected behaviors in state machines.
  - **[Exploratory Testing](https://naodeng.com.cn/en/wiki/exploratory-testing)** : While performing exploratory testing, leverage error guessing to direct the exploration towards areas with suspected high risk.
  - **Automated [Regression Testing](https://naodeng.com.cn/en/wiki/regression-testing)** : Integrate error guesses as additional test cases to catch regressions in areas known to be fragile.

### Practical Application

#### Can you provide examples of situations where error guessing would be particularly useful?

  [Error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is particularly useful in scenarios where:

  - **Complex user inputs**
    are expected, such as free-form text fields where input patterns are unpredictable and could lead to unexpected behaviors.

  - **Boundary conditions**
    are not clearly defined, and testers must rely on intuition to identify potential edge cases.

  - **Historical data**
    indicates frequent issues in certain areas, suggesting that similar problems might reoccur in those or related components.

  - **Intermittent issues**
    are reported, which might be difficult to reproduce systematically but can be triggered based on a tester's hunch about what might be causing the problem.

  - **Third-party integrations**
    are involved, and the tester has to anticipate issues that could arise from external systems' unpredictable behavior.

  - **New features**
    are introduced without detailed requirements, and testers must use their experience to guess where errors might occur.

  - **Legacy systems**
    are updated or modified, and there is a lack of comprehensive documentation or understanding of the system's intricacies.
  In these situations, [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) can guide the creation of [test cases](https://naodeng.com.cn/en/wiki/test-case) that target less obvious failure points, supplementing more structured testing methods. It's a technique that leverages the tester's intuition and experience to foresee and test for potential errors that might not be immediately apparent through formal testing strategies.

  - **Complex user inputs**
    are expected, such as free-form text fields where input patterns are unpredictable and could lead to unexpected behaviors.

  - **Boundary conditions**
    are not clearly defined, and testers must rely on intuition to identify potential edge cases.

  - **Historical data**
    indicates frequent issues in certain areas, suggesting that similar problems might reoccur in those or related components.

  - **Intermittent issues**
    are reported, which might be difficult to reproduce systematically but can be triggered based on a tester's hunch about what might be causing the problem.

  - **Third-party integrations**
    are involved, and the tester has to anticipate issues that could arise from external systems' unpredictable behavior.

  - **New features**
    are introduced without detailed requirements, and testers must use their experience to guess where errors might occur.

  - **Legacy systems**
    are updated or modified, and there is a lack of comprehensive documentation or understanding of the system's intricacies.

#### How can error guessing be applied in automated testing?

  [Error guessing](https://naodeng.com.cn/en/wiki/error-guessing) can be effectively applied in [automated testing](https://naodeng.com.cn/en/wiki/automated-testing) by incorporating **heuristic-based checks** into [test scripts](https://naodeng.com.cn/en/wiki/test-script). Experienced testers can use their intuition to predict potential error conditions and then write automated tests to validate these scenarios.
  For instance, if a tester suspects that an application might not handle unexpected file formats correctly, they could write an automated test that attempts to upload various incorrect file formats and assert that the application responds appropriately.

  ```
  describe('File Upload Error Handling', () => {
    const invalidFormats = ['invalidimage.bmp', 'randomtext.txt', 'corruptedfile.jpg'];
    invalidFormats.forEach((format) => {
      it(`should reject the ${format} file format`, () => {
        const response = uploadFile(format);
        expect(response).to.have.status(400);
        expect(response).to.have.error('Unsupported file format');
      });
    });
  });
  ```
  Automated tests based on [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) can be **randomized** to cover a wider range of inputs or scenarios, using tools like property-based testing frameworks. This approach can uncover errors that are not easily anticipated through formal [test case](https://naodeng.com.cn/en/wiki/test-case) design.
  To maximize the effectiveness, [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) should be **continuously refined** based on the feedback from automated test results. As the system evolves and new insights are gained, the automated tests should be updated to reflect the latest understanding of potential error conditions.
  Incorporating [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) into [automated testing](https://naodeng.com.cn/en/wiki/automated-testing) requires a balance between **exploratory insight** and **systematic execution**, leveraging the speed and repeatability of automation while capitalizing on the tester's experience and intuition.

#### What types of errors are typically identified using error guessing?

  [Error guessing](https://naodeng.com.cn/en/wiki/error-guessing) typically identifies errors that are not easily captured by formal testing methods. These include:

  - **Boundary-related errors** : Guessing values at the extreme ends of input ranges that might not be covered by equivalence partitioning or boundary value analysis.
  - **User behavior errors** : Anticipating mistakes users might make, such as entering incorrect data types or sequences of actions that could cause the system to fail.
  - **Concurrency issues** : Identifying race conditions and deadlocks that might occur when multiple processes access shared resources.
  - **Resource exhaustion** : Guessing scenarios where the system might run out of memory, disk space, or other resources.
  - **Error handling paths** : Identifying untested paths that occur when the system encounters an error condition.
  - **Integration errors** : Guessing how components might fail to interact correctly, especially when they have not been integrated before.
  - **Security vulnerabilities** : Anticipating ways an attacker might exploit the system, such as SQL injection or buffer overflows.
  Experienced testers use their knowledge of the system, its environment, and potential user behavior to make educated guesses about where these types of errors might occur. While [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) is less systematic than other testing techniques, it can uncover issues that might otherwise be missed.

  - **Boundary-related errors** : Guessing values at the extreme ends of input ranges that might not be covered by equivalence partitioning or boundary value analysis.
  - **User behavior errors** : Anticipating mistakes users might make, such as entering incorrect data types or sequences of actions that could cause the system to fail.
  - **Concurrency issues** : Identifying race conditions and deadlocks that might occur when multiple processes access shared resources.
  - **Resource exhaustion** : Guessing scenarios where the system might run out of memory, disk space, or other resources.
  - **Error handling paths** : Identifying untested paths that occur when the system encounters an error condition.
  - **Integration errors** : Guessing how components might fail to interact correctly, especially when they have not been integrated before.
  - **Security vulnerabilities** : Anticipating ways an attacker might exploit the system, such as SQL injection or buffer overflows.

#### How can the effectiveness of error guessing be measured?

  Measuring the effectiveness of **[error guessing](https://naodeng.com.cn/en/wiki/error-guessing)** can be challenging due to its subjective nature. However, you can gauge its success through several indicators:

  - **Defect Detection Ratio (DDR)**: Compare the number of defects found through [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) to the total number of defects found. A higher ratio indicates more effectiveness.

    ```
    DDR = (Defects found by error guessing / Total defects found) * 100
    ```

  - **Defect Detection Efficiency (DDE)**: Assess how quickly [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) identifies defects compared to other methods. Faster detection can suggest higher efficiency.

    ```
    DDE = (Defects found by error guessing / Time spent on error guessing)
    ```

  - **[Severity](https://naodeng.com.cn/en/wiki/severity) of Defects**: Evaluate the [severity](https://naodeng.com.cn/en/wiki/severity) of defects caught by [error guessing](https://naodeng.com.cn/en/wiki/error-guessing). Catching critical defects can reflect the technique's value.
  - **[Test Coverage](https://naodeng.com.cn/en/wiki/test-coverage)**: Analyze whether [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) leads to identifying areas not covered by existing [test cases](https://naodeng.com.cn/en/wiki/test-case).
  - **Feedback from Retrospectives**: Collect qualitative data from team retrospectives on the impact of [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) on the testing process.
  - **Historical Comparison**: Compare current project metrics with past projects where [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) was not employed.
  To ensure a more objective assessment, combine these metrics with data from other testing techniques. This approach helps in understanding the overall contribution of [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) to the [test strategy](https://naodeng.com.cn/en/wiki/test-strategy). Remember, the goal is to complement, not replace, systematic testing methods with [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) insights.

  - **Defect Detection Ratio (DDR)**: Compare the number of defects found through [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) to the total number of defects found. A higher ratio indicates more effectiveness.

    ```
    DDR = (Defects found by error guessing / Total defects found) * 100
    ```

  - **Defect Detection Efficiency (DDE)**: Assess how quickly [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) identifies defects compared to other methods. Faster detection can suggest higher efficiency.

    ```
    DDE = (Defects found by error guessing / Time spent on error guessing)
    ```

  - **[Severity](https://naodeng.com.cn/en/wiki/severity) of Defects**: Evaluate the [severity](https://naodeng.com.cn/en/wiki/severity) of defects caught by [error guessing](https://naodeng.com.cn/en/wiki/error-guessing). Catching critical defects can reflect the technique's value.
  - **[Test Coverage](https://naodeng.com.cn/en/wiki/test-coverage)**: Analyze whether [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) leads to identifying areas not covered by existing [test cases](https://naodeng.com.cn/en/wiki/test-case).
  - **Feedback from Retrospectives**: Collect qualitative data from team retrospectives on the impact of [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) on the testing process.
  - **Historical Comparison**: Compare current project metrics with past projects where [error guessing](https://naodeng.com.cn/en/wiki/error-guessing) was not employed.
