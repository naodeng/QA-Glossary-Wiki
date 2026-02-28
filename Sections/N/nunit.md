# NUnit


<!-- TOC START -->
- [Related Terms:](#related-terms)
  - [See also:](#see-also)
- [Questions about NUnit ?](#questions-about-nunit)
  - [Basics and Importance](#basics-and-importance)
    - [What is NUnit?](#what-is-nunit)
    - [Why is NUnit important in software testing?](#why-is-nunit-important-in-software-testing)
    - [What are the key features of NUnit?](#what-are-the-key-features-of-nunit)
    - [How does NUnit compare to other testing frameworks?](#how-does-nunit-compare-to-other-testing-frameworks)
  - [Installation and Setup](#installation-and-setup)
    - [How do you install NUnit?](#how-do-you-install-nunit)
    - [What are the system requirements for NUnit?](#what-are-the-system-requirements-for-nunit)
    - [How do you set up NUnit for a new project?](#how-do-you-set-up-nunit-for-a-new-project)
    - [What are the common issues faced during NUnit installation and how can they be resolved?](#what-are-the-common-issues-faced-during-nunit-installation-and-how-can-they-be-resolved)
  - [Usage and Implementation](#usage-and-implementation)
    - [How do you write a basic test case in NUnit?](#how-do-you-write-a-basic-test-case-in-nunit)
    - [What are the different types of assertions in NUnit?](#what-are-the-different-types-of-assertions-in-nunit)
    - [How do you group tests in NUnit?](#how-do-you-group-tests-in-nunit)
    - [How can you run a specific set of tests in NUnit?](#how-can-you-run-a-specific-set-of-tests-in-nunit)
    - [What is the use of SetUp and TearDown in NUnit?](#what-is-the-use-of-setup-and-teardown-in-nunit)
  - [Advanced Concepts](#advanced-concepts)
    - [How does NUnit handle exceptions?](#how-does-nunit-handle-exceptions)
    - [What is parameterized testing in NUnit?](#what-is-parameterized-testing-in-nunit)
    - [How can you implement data-driven testing in NUnit?](#how-can-you-implement-data-driven-testing-in-nunit)
    - [What is the role of TestFixture in NUnit?](#what-is-the-role-of-testfixture-in-nunit)
    - [How can you integrate NUnit with other tools like Selenium for e2e testing?](#how-can-you-integrate-nunit-with-other-tools-like-selenium-for-e2e-testing)
<!-- TOC END -->

NUnit

is an open-source

unit testing

framework for C# derived from JUnit. It facilitates writing and executing tests in .NET, with tools like

NUnit

-console.exe for batch

test executions

.

## Related Terms:

- [JUnit Testing](../J/junit-testing.md)
- [Test Framework](../T/test-framework.md)

### See also:

- [Official Website](https://nunit.org/)
- [Wikipedia](https://en.wikipedia.org/wiki/NUnit)

## Questions about NUnit ?

### Basics and Importance

#### What is NUnit?

  [NUnit](../N/nunit.md) is an open-source **[unit testing](../U/unit-testing.md) framework** for .NET languages, designed to be a flexible and user-friendly tool for writing and running tests. It is part of the .NET Foundation and is widely used for its ability to create both simple and complex [test cases](../T/test-case.md).
  Tests in [NUnit](../N/nunit.md) are created by annotating methods with attributes such as `[Test]` to indicate test methods, `[TestFixture]` to denote test classes, and `[SetUp]` and `[TearDown]` for methods that run before and after each test, respectively. [NUnit](../N/nunit.md) provides a rich set of assertions, like `Assert.AreEqual` and `Assert.IsTrue`, to validate test outcomes.
  To run a specific set of tests, you can use the `--where` option in the [NUnit](../N/nunit.md) console runner or categorize tests using the `[Category]` attribute and filter them accordingly. Exception handling in [NUnit](../N/nunit.md) is straightforward; you can expect exceptions using the `Assert.Throws` method or the `ExpectedException` attribute.
  [Parameterized testing](../P/parameterized-testing.md) is supported through attributes like `[TestCase]` and `[TestCaseSource]`, enabling data-driven testing. For integration with tools like [Selenium](../S/selenium.md), [NUnit](../N/nunit.md) works seamlessly, allowing for [end-to-end testing](../E/end-to-end-testing.md) scenarios.
  [NUnit](../N/nunit.md)'s `[TestFixture]` attribute plays a crucial role in indicating a class contains tests and can also be used to pass parameters for running tests with different inputs.
  To summarize, [NUnit](../N/nunit.md) is a powerful and essential tool in the .NET testing ecosystem, providing a comprehensive suite of features for effective [test automation](../T/test-automation.md).

#### Why is NUnit important in software testing?

  [NUnit](../N/nunit.md) plays a crucial role in [software testing](../S/software-testing.md) by providing a **flexible and efficient** framework to write and execute tests. As a [unit testing](../U/unit-testing.md) framework, it's instrumental in facilitating **[Test-Driven Development](../T/test-driven-development.md) (TDD)**, where tests are written before the actual code, ensuring that software components work as intended from the outset. [NUnit](../N/nunit.md)'s importance also stems from its ability to integrate with **Continuous Integration (CI)** systems, allowing for automated builds and testing, which leads to early detection of defects and regressions.
  Moreover, [NUnit](../N/nunit.md) supports **parallel [test execution](../T/test-execution.md)**, significantly reducing the time required to run extensive [test suites](../T/test-suite.md) and providing quick feedback to developers. Its **extensibility** allows for customization and addition of new features through plugins, making it adaptable to various testing needs. [NUnit](../N/nunit.md)'s **assertion library** is comprehensive, enabling testers to validate a wide range of conditions, which is vital for ensuring code quality and functionality.
  In environments where multiple developers or teams are involved, [NUnit](../N/nunit.md) helps maintain **consistency** in testing approaches, thanks to its well-defined structure and conventions. This consistency is key to understanding and maintaining tests written by different team members. By enforcing good testing practices and providing a platform for robust test creation, [NUnit](../N/nunit.md) significantly contributes to the overall **[quality assurance](../Q/quality-assurance.md)** process in software development.

#### What are the key features of NUnit?

  [NUnit](../N/nunit.md) offers a range of key features that make it a powerful tool for [test automation](../T/test-automation.md):

  - **Attribute-Based Test Configuration**: Tests are easy to configure with attributes such as `[Test]`, `[TestCase]`, and `[TestFixture]` to denote test methods and classes.
  - **[Test Cases](../T/test-case.md) and [Test Suites](../T/test-suite.md)**: Organize tests into cases and suites for better management and structure.
  - **Assert Class**: A comprehensive set of `Assert` methods for validating test outcomes, including multiple overloads for different data types and conditions.
  - **Test [Setup](../S/setup.md) and Teardown**: Utilize `[SetUp]` and `[TearDown]` attributes to prepare and clean up the [test environment](../T/test-environment.md) before and after each test.
  - **Parameterized Tests**: Create tests that run with different sets of data using `[TestCase]` and `[TestCaseSource]` attributes.
  - **Parallel [Test Execution](../T/test-execution.md)**: Run tests in parallel to reduce execution time with the `[Parallelizable]` attribute.
  - **Categories**: Group tests using `[Category]` attribute, allowing selective test running based on categories.
  - **Test Filtering**: Execute a subset of tests using [NUnit](../N/nunit.md)'s powerful test selection language, which allows filtering by name, category, property, or other criteria.
  - **Result Reporting**: Generate detailed test result reports in various formats, including XML, which can be used for further analysis or integration with CI/CD tools.
  - **Platform and Runtime Support**: Compatible with multiple platforms and runtimes, including .NET Core and Mono, enabling cross-platform testing.
  - **Extensibility**: Extend [NUnit](../N/nunit.md) through custom attributes, constraints, and event listeners to tailor it to specific testing needs.
  - **Integration with Various IDEs and CI Tools**: Works seamlessly with popular development environments and continuous integration servers, enhancing the development workflow.
  These features collectively enable [test automation](../T/test-automation.md) engineers to write, organize, and execute tests efficiently, making [NUnit](../N/nunit.md) a versatile choice for many testing scenarios.

  - **Attribute-Based Test Configuration**: Tests are easy to configure with attributes such as `[Test]`, `[TestCase]`, and `[TestFixture]` to denote test methods and classes.
  - **[Test Cases](../T/test-case.md) and [Test Suites](../T/test-suite.md)**: Organize tests into cases and suites for better management and structure.
  - **Assert Class**: A comprehensive set of `Assert` methods for validating test outcomes, including multiple overloads for different data types and conditions.
  - **Test [Setup](../S/setup.md) and Teardown**: Utilize `[SetUp]` and `[TearDown]` attributes to prepare and clean up the [test environment](../T/test-environment.md) before and after each test.
  - **Parameterized Tests**: Create tests that run with different sets of data using `[TestCase]` and `[TestCaseSource]` attributes.
  - **Parallel [Test Execution](../T/test-execution.md)**: Run tests in parallel to reduce execution time with the `[Parallelizable]` attribute.
  - **Categories**: Group tests using `[Category]` attribute, allowing selective test running based on categories.
  - **Test Filtering**: Execute a subset of tests using [NUnit](../N/nunit.md)'s powerful test selection language, which allows filtering by name, category, property, or other criteria.
  - **Result Reporting**: Generate detailed test result reports in various formats, including XML, which can be used for further analysis or integration with CI/CD tools.
  - **Platform and Runtime Support**: Compatible with multiple platforms and runtimes, including .NET Core and Mono, enabling cross-platform testing.
  - **Extensibility**: Extend [NUnit](../N/nunit.md) through custom attributes, constraints, and event listeners to tailor it to specific testing needs.
  - **Integration with Various IDEs and CI Tools**: Works seamlessly with popular development environments and continuous integration servers, enhancing the development workflow.

#### How does NUnit compare to other testing frameworks?

  [NUnit](../N/nunit.md) is a popular testing framework within the .NET ecosystem, often compared to other frameworks like **MSTest** and **xUnit**.
  **MSTest**, Microsoft's official testing framework, is tightly integrated with Visual Studio, offering a smooth experience for developers working within this IDE. However, [NUnit](../N/nunit.md) tends to be more flexible and feature-rich, with a broader range of attributes for [test cases](../T/test-case.md) and better support for parameterized tests. [NUnit](../N/nunit.md)'s assertion library is also considered more powerful. MSTest has improved over time but is often chosen for its seamless integration with the Microsoft stack rather than for advanced features.
  **xUnit**, another open-source framework, is seen as the successor to [NUnit](../N/nunit.md) by some in the .NET community. It introduces a more modern approach to testing, doing away with [setup](../S/setup.md) and teardown in favor of constructor and dispose methods for test initialization and cleanup. xUnit also boasts better support for asynchronous testing and has a more extensible model for [test case](../T/test-case.md) discovery and execution. However, [NUnit](../N/nunit.md)'s widespread use and familiarity remain strong points for many teams, especially those with existing [NUnit](../N/nunit.md) [test suites](../T/test-suite.md).
  In summary, [NUnit](../N/nunit.md) offers a balance between the ease of use provided by MSTest and the modern testing approaches of xUnit. It stands out for its flexibility, extensive assertion library, and strong support for data-driven testing, making it a solid choice for many .NET developers. However, the choice between these frameworks often comes down to specific project needs, team familiarity, and integration requirements.

### Installation and Setup

#### How do you install NUnit?

  To install [NUnit](../N/nunit.md), you can use NuGet Package Manager, which is the simplest and most common method for .NET projects. Follow these steps:

  1. Open your project in Visual Studio.
  2. Go to the
    **Solution Explorer**
    .

  3. Right-click on the project where you want to add NUnit.
  4. Select
    **Manage NuGet Packages**
    .

  5. In the NuGet Package Manager, click on the
    **Browse**
    tab.

  6. Search for
    `NUnit`
    .

  7. Select the
    `NUnit`
    package from the list.

  8. Click on the
    **Install**
    button to add NUnit to your project.
  Alternatively, you can use the Package Manager Console to install [NUnit](../N/nunit.md):

  ```
  Install-Package NUnit -Version 3.x.x
  ```
  Replace `3.x.x` with the desired version number.
  For .NET Core or .NET Standard projects, you can also use the `dotnet` CLI:

  ```
  dotnet add package NUnit --version 3.x.x
  ```
  Again, replace `3.x.x` with the specific version you want to install.
  Ensure that your project's target framework is compatible with the version of [NUnit](../N/nunit.md) you are installing. After installation, you can start writing your tests using the [NUnit](../N/nunit.md) framework. Remember to also install the `NUnit3TestAdapter` if you want to run tests within Visual Studio's Test Explorer.

  1. Open your project in Visual Studio.
  2. Go to the
    **Solution Explorer**
    .

  3. Right-click on the project where you want to add NUnit.
  4. Select
    **Manage NuGet Packages**
    .

  5. In the NuGet Package Manager, click on the
    **Browse**
    tab.

  6. Search for
    `NUnit`
    .

  7. Select the
    `NUnit`
    package from the list.

  8. Click on the
    **Install**
    button to add NUnit to your project.

#### What are the system requirements for NUnit?

  [NUnit](../N/nunit.md)'s system requirements vary depending on the version you're using. For **[NUnit](../N/nunit.md) 3**, the requirements are as follows:

  - **.NET Framework** : NUnit is compatible with .NET Framework 2.0 and newer. However, to use the latest features and for the best experience, .NET Framework 4.5 or above is recommended.
  - **.NET Core** : NUnit supports .NET Core 1.1 and newer, including .NET 5 and 6 for cross-platform testing.
  - **Mono** : For running on platforms that support Mono, version 4.6 or later is required.
  - **Operating System** : NUnit is cross-platform and can run on Windows, macOS, and Linux.
  - **IDE Support** : NUnit works with various Integrated Development Environments (IDEs) like Visual Studio, which requires the NUnit 3 Test Adapter for integration.
  Ensure that the appropriate version of the .NET platform is installed on your system before installing [NUnit](../N/nunit.md). For projects targeting multiple frameworks, ensure that all target frameworks meet the minimum requirements.

  ```
  <ItemGroup>
    <PackageReference Include="NUnit" Version="3.x.x" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="x.x.x" />
    <PackageReference Include="NUnit3TestAdapter" Version="x.x.x" />
  </ItemGroup>
  ```
  Replace `3.x.x` with the specific version of [NUnit](../N/nunit.md) you wish to use, and `x.x.x` with the versions of the test SDK and test adapter that are compatible with your development environment.

  - **.NET Framework** : NUnit is compatible with .NET Framework 2.0 and newer. However, to use the latest features and for the best experience, .NET Framework 4.5 or above is recommended.
  - **.NET Core** : NUnit supports .NET Core 1.1 and newer, including .NET 5 and 6 for cross-platform testing.
  - **Mono** : For running on platforms that support Mono, version 4.6 or later is required.
  - **Operating System** : NUnit is cross-platform and can run on Windows, macOS, and Linux.
  - **IDE Support** : NUnit works with various Integrated Development Environments (IDEs) like Visual Studio, which requires the NUnit 3 Test Adapter for integration.

#### How do you set up NUnit for a new project?

  To set up [NUnit](../N/nunit.md) for a new project, follow these steps:

  1. **Create a new project** in your preferred IDE (e.g., Visual Studio).
  2. **Install the [NUnit](../N/nunit.md) framework** using your project's package manager. For .NET Core or .NET 5+ projects, use the following command in the Package Manager Console:
    Alternatively, for .NET Framework projects or if you prefer to use the .NET CLI, use:

    ```
    Install-Package NUnit
    ```

    ```
    dotnet add package NUnit
    ```

  3. **Install the [NUnit](../N/nunit.md) test adapter**, which allows the [test runner](../T/test-runner.md) to execute your tests. Use the following command:
    Or, for the .NET CLI:

    ```
    Install-Package NUnit3TestAdapter
    ```

    ```
    dotnet add package NUnit3TestAdapter
    ```

  4. **Reference the [NUnit](../N/nunit.md) framework** in your test project by adding a `using NUnit.Framework;` directive at the top of your test files.
  5. **Create a [test class](../T/test-class.md)** and decorate it with `[TestFixture]`. Inside the class, define test methods and annotate them with `[Test]`.
  6. **Build the project** to compile the [test cases](../T/test-case.md).
  7. **Run the tests** using the test explorer in your IDE or via the command line. For the command line, navigate to your project directory and run:

    ```
    dotnet test
    ```
  Ensure that your project targets a compatible framework version for [NUnit](../N/nunit.md). If you encounter issues, verify that the [NUnit](../N/nunit.md) and test adapter versions are compatible with your project's target framework.

  1. **Create a new project** in your preferred IDE (e.g., Visual Studio).
  2. **Install the [NUnit](../N/nunit.md) framework** using your project's package manager. For .NET Core or .NET 5+ projects, use the following command in the Package Manager Console:
    Alternatively, for .NET Framework projects or if you prefer to use the .NET CLI, use:

    ```
    Install-Package NUnit
    ```

    ```
    dotnet add package NUnit
    ```

  3. **Install the [NUnit](../N/nunit.md) test adapter**, which allows the [test runner](../T/test-runner.md) to execute your tests. Use the following command:
    Or, for the .NET CLI:

    ```
    Install-Package NUnit3TestAdapter
    ```

    ```
    dotnet add package NUnit3TestAdapter
    ```

  4. **Reference the [NUnit](../N/nunit.md) framework** in your test project by adding a `using NUnit.Framework;` directive at the top of your test files.
  5. **Create a [test class](../T/test-class.md)** and decorate it with `[TestFixture]`. Inside the class, define test methods and annotate them with `[Test]`.
  6. **Build the project** to compile the [test cases](../T/test-case.md).
  7. **Run the tests** using the test explorer in your IDE or via the command line. For the command line, navigate to your project directory and run:

    ```
    dotnet test
    ```

#### What are the common issues faced during NUnit installation and how can they be resolved?

  Common issues during [NUnit](../N/nunit.md) installation and their resolutions include:

  - **Compatibility Issues**: Ensure that the [NUnit](../N/nunit.md) version is compatible with the .NET framework version in your project. If there's a mismatch, update your project's framework or select a compatible [NUnit](../N/nunit.md) version.
  - **NuGet Package Manager Problems**: Sometimes, the NuGet package manager might not work as expected. Try clearing the NuGet cache using the command:
    or reinstall the [NUnit](../N/nunit.md) package.

    ```
    nuget locals all -clear
    ```

  - **Incorrect Installation**: [NUnit](../N/nunit.md) should be installed as a NuGet package within your test project, not as a standalone application. Use the Package Manager Console:
    or the NuGet Package Manager GUI in Visual Studio.

    ```
    Install-Package NUnit
    ```

  - **Missing [NUnit](../N/nunit.md) Test Adapter**: Without the [NUnit](../N/nunit.md) Test Adapter, Visual Studio won't recognize or run your tests. Install it via NuGet:

    ```
    Install-Package NUnit3TestAdapter
    ```

  - **Path Issues**: If [NUnit](../N/nunit.md) is installed globally, ensure that the path to the [NUnit](../N/nunit.md) console runner is added to your system's PATH environment variable.
  - **Access Permissions**: Lack of proper access permissions can cause installation failure. Run your IDE as an administrator or ensure your user has the necessary permissions.
  - **Firewall or Antivirus Interference**: Sometimes, firewall or antivirus settings can prevent [NUnit](../N/nunit.md) from installing correctly. Temporarily disable these or add an exception for [NUnit](../N/nunit.md).
  - **Corrupted Installation Files**: If the installation files are corrupted, re-download the [NUnit](../N/nunit.md) package or use a different source.
  If issues persist, consult the [NUnit](../N/nunit.md) documentation or community forums for specific error messages or troubleshooting steps.

  - **Compatibility Issues**: Ensure that the [NUnit](../N/nunit.md) version is compatible with the .NET framework version in your project. If there's a mismatch, update your project's framework or select a compatible [NUnit](../N/nunit.md) version.
  - **NuGet Package Manager Problems**: Sometimes, the NuGet package manager might not work as expected. Try clearing the NuGet cache using the command:
    or reinstall the [NUnit](../N/nunit.md) package.

    ```
    nuget locals all -clear
    ```

  - **Incorrect Installation**: [NUnit](../N/nunit.md) should be installed as a NuGet package within your test project, not as a standalone application. Use the Package Manager Console:
    or the NuGet Package Manager GUI in Visual Studio.

    ```
    Install-Package NUnit
    ```

  - **Missing [NUnit](../N/nunit.md) Test Adapter**: Without the [NUnit](../N/nunit.md) Test Adapter, Visual Studio won't recognize or run your tests. Install it via NuGet:

    ```
    Install-Package NUnit3TestAdapter
    ```

  - **Path Issues**: If [NUnit](../N/nunit.md) is installed globally, ensure that the path to the [NUnit](../N/nunit.md) console runner is added to your system's PATH environment variable.
  - **Access Permissions**: Lack of proper access permissions can cause installation failure. Run your IDE as an administrator or ensure your user has the necessary permissions.
  - **Firewall or Antivirus Interference**: Sometimes, firewall or antivirus settings can prevent [NUnit](../N/nunit.md) from installing correctly. Temporarily disable these or add an exception for [NUnit](../N/nunit.md).
  - **Corrupted Installation Files**: If the installation files are corrupted, re-download the [NUnit](../N/nunit.md) package or use a different source.

### Usage and Implementation

#### How do you write a basic test case in NUnit?

  To write a basic [test case](../T/test-case.md) in [NUnit](../N/nunit.md), follow these steps:

  1. **Create a [test class](../T/test-class.md)** by marking a class with the `[TestFixture]` attribute. This class will contain your test methods.

    ```
    [TestFixture]
    public class CalculatorTests
    {
    }
    ```

  2. **Define a test method** within the [test class](../T/test-class.md) by marking a method with the `[Test]` attribute. This method will represent an individual [test case](../T/test-case.md).

    ```
    [Test]
    public void Add_TwoNumbers_ReturnsSum()
    {
    }
    ```

  3. **Implement the test logic** inside the test method. Instantiate the class under test, perform operations, and use assertions to validate the expected outcome.

    ```
    [Test]
    public void Add_TwoNumbers_ReturnsSum()
    {
        // Arrange
        var calculator = new Calculator();
        int number1 = 5;
        int number2 = 7;
        // Act
        int result = calculator.Add(number1, number2);
        // Assert
        Assert.AreEqual(12, result);
    }
    ```

  4. **Run the test** using [NUnit](../N/nunit.md)'s [test runner](../T/test-runner.md) or an integrated development environment (IDE) that supports [NUnit](../N/nunit.md). The [test runner](../T/test-runner.md) will execute the test method and report the outcome.
  Remember to **keep tests isolated** and **independent** from each other. Each test should focus on a single behavior or scenario. Use `[SetUp]` and `[TearDown]` methods if you need to perform common [setup](../S/setup.md) or cleanup tasks for each test.

  1. **Create a [test class](../T/test-class.md)** by marking a class with the `[TestFixture]` attribute. This class will contain your test methods.

    ```
    [TestFixture]
    public class CalculatorTests
    {
    }
    ```

  2. **Define a test method** within the [test class](../T/test-class.md) by marking a method with the `[Test]` attribute. This method will represent an individual [test case](../T/test-case.md).

    ```
    [Test]
    public void Add_TwoNumbers_ReturnsSum()
    {
    }
    ```

  3. **Implement the test logic** inside the test method. Instantiate the class under test, perform operations, and use assertions to validate the expected outcome.

    ```
    [Test]
    public void Add_TwoNumbers_ReturnsSum()
    {
        // Arrange
        var calculator = new Calculator();
        int number1 = 5;
        int number2 = 7;
        // Act
        int result = calculator.Add(number1, number2);
        // Assert
        Assert.AreEqual(12, result);
    }
    ```

  4. **Run the test** using [NUnit](../N/nunit.md)'s [test runner](../T/test-runner.md) or an integrated development environment (IDE) that supports [NUnit](../N/nunit.md). The [test runner](../T/test-runner.md) will execute the test method and report the outcome.

#### What are the different types of assertions in NUnit?

  [NUnit](../N/nunit.md) provides a variety of assertions to validate test outcomes. These assertions are categorized into:

  - **Equality Assertions**: Verify if two values are equal or not.

    ```
    Assert.AreEqual(expected, actual);
    Assert.AreNotEqual(notExpected, actual);
    ```

  - **Identity Assertions**: Check if two object instances are the same.

    ```
    Assert.AreSame(expected, actual);
    Assert.AreNotSame(notExpected, actual);
    ```

  - **Boolean Assertions**: Test for `true` or `false` conditions.

    ```
    Assert.IsTrue(condition);
    Assert.IsFalse(condition);
    ```

  - **Nullability Assertions**: Determine if an object is `null` or not.

    ```
    Assert.IsNull(object);
    Assert.IsNotNull(object);
    ```

  - **Comparison Assertions**: Compare values to determine relative size.

    ```
    Assert.Greater(value1, value2);
    Assert.GreaterOrEqual(value1, value2);
    Assert.Less(value1, value2);
    Assert.LessOrEqual(value1, value2);
    ```

  - **String Assertions**: Specific to string operations like containment, matching, etc.

    ```
    Assert.AreEqual(expected, actual, ignoreCase, message);
    Assert.Contains(substring, string);
    Assert.StartsWith(substring, string);
    Assert.EndsWith(substring, string);
    Assert.IsMatch(regex, string);
    ```

  - **Collection Assertions**: Validate aspects of collections like equality, subsets, etc.

    ```
    Assert.AreEqual(expected, actual, comparer);
    Assert.Contains(object, collection);
    Assert.AllItemsAreInstancesOfType(collection, expectedType);
    Assert.IsSubsetOf(subset, superset);
    ```

  - **Exception Assertions**: Assert that a particular type of exception is thrown.

    ```
    Assert.Throws<ExceptionType>(() => { /* code that throws exception */ });
    Assert.DoesNotThrow(() => { /* code that should not throw exception */ });
    ```

  - **Constraint Model**: A more expressive way of writing assertions using a fluent interface.

    ```
    Assert.That(actual, Is.EqualTo(expected));
    Assert.That(actual, Is.Not.Null);
    Assert.That(collection, Has.No.Member(item));
    Assert.That(() => { /* code */ }, Throws.TypeOf<ExceptionType>());
    ```
  These assertions help in validating the behavior of the code under test, ensuring that the software behaves as expected.

  - **Equality Assertions**: Verify if two values are equal or not.

    ```
    Assert.AreEqual(expected, actual);
    Assert.AreNotEqual(notExpected, actual);
    ```

  - **Identity Assertions**: Check if two object instances are the same.

    ```
    Assert.AreSame(expected, actual);
    Assert.AreNotSame(notExpected, actual);
    ```

  - **Boolean Assertions**: Test for `true` or `false` conditions.

    ```
    Assert.IsTrue(condition);
    Assert.IsFalse(condition);
    ```

  - **Nullability Assertions**: Determine if an object is `null` or not.

    ```
    Assert.IsNull(object);
    Assert.IsNotNull(object);
    ```

  - **Comparison Assertions**: Compare values to determine relative size.

    ```
    Assert.Greater(value1, value2);
    Assert.GreaterOrEqual(value1, value2);
    Assert.Less(value1, value2);
    Assert.LessOrEqual(value1, value2);
    ```

  - **String Assertions**: Specific to string operations like containment, matching, etc.

    ```
    Assert.AreEqual(expected, actual, ignoreCase, message);
    Assert.Contains(substring, string);
    Assert.StartsWith(substring, string);
    Assert.EndsWith(substring, string);
    Assert.IsMatch(regex, string);
    ```

  - **Collection Assertions**: Validate aspects of collections like equality, subsets, etc.

    ```
    Assert.AreEqual(expected, actual, comparer);
    Assert.Contains(object, collection);
    Assert.AllItemsAreInstancesOfType(collection, expectedType);
    Assert.IsSubsetOf(subset, superset);
    ```

  - **Exception Assertions**: Assert that a particular type of exception is thrown.

    ```
    Assert.Throws<ExceptionType>(() => { /* code that throws exception */ });
    Assert.DoesNotThrow(() => { /* code that should not throw exception */ });
    ```

  - **Constraint Model**: A more expressive way of writing assertions using a fluent interface.

    ```
    Assert.That(actual, Is.EqualTo(expected));
    Assert.That(actual, Is.Not.Null);
    Assert.That(collection, Has.No.Member(item));
    Assert.That(() => { /* code */ }, Throws.TypeOf<ExceptionType>());
    ```

#### How do you group tests in NUnit?

  In [NUnit](../N/nunit.md), tests can be grouped using **attributes** to organize and manage them effectively. The primary attribute used for grouping is `[TestFixture]`, which denotes a class that contains test methods. Within a test fixture, you can further group tests using the `[Category]` attribute.
  Here's an example of using `[Category]` to group tests:

  ```
  [TestFixture]
  public class MathTests
  {
      [Test]
      [Category("Addition")]
      public void Add_PositiveNumbers_ReturnsCorrectSum()
      {
          // Test code here
      }
      [Test]
      [Category("Subtraction")]
      public void Subtract_PositiveNumbers_ReturnsCorrectDifference()
      {
          // Test code here
      }
  }
  ```
  You can also apply multiple categories to a single test:

  ```
  [Test]
  [Category("Addition")]
  [Category("Boundary")]
  public void Add_MaxIntValues_ReturnsOverflow()
  {
      // Test code here
  }
  ```
  To run a specific group of tests, use the `--where` command-line option with the `cat` keyword followed by the category name:

  ```
  nunit-console --where "cat == Addition" MyTests.dll
  ```
  For more complex grouping, you can use **[NUnit](../N/nunit.md)'s Test Selection Language** to include or exclude tests based on multiple categories or other properties.
  Remember that grouping tests helps in executing a subset of tests based on their category, which is useful for targeting specific areas of the application during testing. It also aids in maintaining a well-organized [test suite](../T/test-suite.md).

#### How can you run a specific set of tests in NUnit?

  To run a specific set of tests in [NUnit](../N/nunit.md), you can use the **Test Selection Language** or **command-line options** provided by the [NUnit](../N/nunit.md) Console Runner or the [NUnit](../N/nunit.md) Test Adapter for IDEs like Visual Studio.
  **Using Test Selection Language:**
  [NUnit](../N/nunit.md)'s Test Selection Language allows you to select tests based on their properties, such as name, category, or custom properties. For example, to run tests by name:

  ```
  nunit3-console.exe --where "test==MyNamespace.MyTestClass.MyTestMethod" path\to\test\assembly.dll
  ```
  To run tests belonging to a specific category:

  ```
  nunit3-console.exe --where "cat==Urgent" path\to\test\assembly.dll
  ```
  **Using Command-Line Options:**
  When using the [NUnit](../N/nunit.md) Console Runner, you can specify the tests to run by their fully qualified names:

  ```
  nunit3-console.exe --test=MyNamespace.MyTestClass.MyTestMethod path\to\test\assembly.dll
  ```
  You can also run multiple tests by separating them with commas:

  ```
  nunit3-console.exe --test=MyNamespace.MyTestClass.MyTestMethod1,MyNamespace.MyTestClass.MyTestMethod2 path\to\test\assembly.dll
  ```
  **Using [NUnit](../N/nunit.md) Test Adapter in Visual Studio:**
  If you're using Visual Studio, you can run a specific set of tests by using the **Test Explorer**. You can filter tests by name, outcome, duration, and traits. Right-click on the test or group of tests you want to run and select **Run**.
  **Note:** Ensure that your tests are properly grouped using attributes like `[Category]` to facilitate easier selection when running specific sets of tests.

#### What is the use of SetUp and TearDown in NUnit?

  In [NUnit](../N/nunit.md), `SetUp` and `TearDown` are attributes that define methods to run before and after each test within a `TestFixture`.
  **`SetUp`** is used to initialize objects or set the state before each test runs. This ensures that every test starts with a known environment, potentially reducing the chance of dependencies between tests.

  ```
  [SetUp]
  public void Initialize()
  {
      // Code to set up test environment
  }
  ```
  **`TearDown`**, on the other hand, is used to clean up after a test has run. This might involve releasing resources, such as closing [database](../D/database.md) connections or deleting [test data](../T/test-data.md), to ensure that no side effects are left that could affect subsequent tests.

  ```
  [TearDown]
  public void Cleanup()
  {
      // Code to clean up after the test
  }
  ```
  Using `SetUp` and `TearDown` helps maintain a clean [test environment](../T/test-environment.md) and can prevent tests from interfering with each other, which is crucial for achieving accurate and reliable test results. They are particularly useful when tests are not independent, sharing resources or state that must be reset. However, it's important to keep these methods as lightweight as possible to minimize the impact on the overall [test suite](../T/test-suite.md) execution time.

### Advanced Concepts

#### How does NUnit handle exceptions?

  [NUnit](../N/nunit.md) handles exceptions using its built-in assertion model, allowing [test automation](../T/test-automation.md) engineers to assert that exceptions are thrown as expected during [test execution](../T/test-execution.md). To verify that a specific exception is thrown, you can use the `Assert.Throws` method or its generic counterpart `Assert.Throws<T>` where `T` is the type of the expected exception. Here's an example:

  ```
  [Test]
  public void ShouldThrowException()
  {
      Assert.Throws<InvalidOperationException>(() =>
      {
          // Code that should throw the InvalidOperationException
      });
  }
  ```
  For cases where you need to further inspect the exception, you can capture it as follows:

  ```
  [Test]
  public void ShouldThrowExceptionWithSpecificProperties()
  {
      var ex = Assert.Throws<InvalidOperationException>(() =>
      {
          // Code that should throw the InvalidOperationException
      });
      Assert.That(ex.Message, Is.EqualTo("Expected message"));
  }
  ```
  If you expect no exception to be thrown, you can use `Assert.DoesNotThrow`:

  ```
  [Test]
  public void ShouldNotThrowException()
  {
      Assert.DoesNotThrow(() =>
      {
          // Code that should not throw any exceptions
      });
  }
  ```
  [NUnit](../N/nunit.md) also provides the `ExpectedException` attribute, but it's considered obsolete in favor of the `Assert.Throws` method, which offers more control and better readability. By using these assertions, you can ensure that your code not only functions correctly under normal conditions but also handles error states as intended.

#### What is parameterized testing in NUnit?

  [Parameterized testing](../P/parameterized-testing.md) in [NUnit](../N/nunit.md) allows you to run the same test multiple times with different sets of input data. This approach is useful for covering a wide range of input combinations without writing multiple test methods. To implement parameterized tests, you can use attributes like `[TestCase]`, `[TestCaseSource]`, or `[ValueSource]`.
  With the `[TestCase]` attribute, you can specify inline parameters directly on the test method. For example:

  ```
  [Test]
  [TestCase(1, 2, 3)]
  [TestCase(3, 3, 6)]
  [TestCase(2, -2, 0)]
  public void AddTest(int a, int b, int expectedSum)
  {
      Assert.AreEqual(expectedSum, Add(a, b));
  }
  ```
  The `[TestCaseSource]` attribute allows you to define a separate method, property, or field that returns an `IEnumerable` of [test cases](../T/test-case.md). This is particularly useful when you have complex data or need to share [test data](../T/test-data.md) across multiple test methods.

  ```
  public static IEnumerable<TestCaseData> AddCases
  {
      get
      {
          yield return new TestCaseData(1, 2).Returns(3);
          yield return new TestCaseData(3, 3).Returns(6);
          // More test cases
      }
  }
  [Test, TestCaseSource(nameof(AddCases))]
  public int AddTest(int a, int b)
  {
      return Add(a, b);
  }
  ```
  The `[ValueSource]` attribute is similar to `[TestCaseSource]` but is used for providing a single parameter to the test method.
  Parameterized tests enhance [test coverage](../T/test-coverage.md) and [maintainability](../M/maintainability.md), as they separate test logic from [test data](../T/test-data.md), allowing for easy updates and additions to [test scenarios](../T/test-scenario.md).

#### How can you implement data-driven testing in NUnit?

  To implement data-driven testing in [NUnit](../N/nunit.md), you can use the `TestCaseSource` attribute to specify a source for your [test data](../T/test-data.md). This source can be a property, field, or method that returns an `IEnumerable`.
  Here's a succinct example:

  ```
  [TestFixture]
  public class DataDrivenTests
  {
      public static IEnumerable<TestCaseData> TestData
      {
          get
          {
              yield return new TestCaseData("input1", "expected1");
              yield return new TestCaseData("input2", "expected2");
              // Add more test cases as needed
          }
      }
      [Test, TestCaseSource(nameof(TestData))]
      public void TestMethod(string input, string expected)
      {
          // Arrange & Act
          var actual = SomeFunction(input);
          // Assert
          Assert.AreEqual(expected, actual);
      }
  }
  ```
  In this example, `TestData` is an `IEnumerable<TestCaseData>` that yields [test cases](../T/test-case.md). Each `TestCaseData` instance represents a set of arguments to be passed to the `TestMethod`.
  **Note**: Ensure that the data source returns objects compatible with the parameters of your test method. [NUnit](../N/nunit.md) will invoke the test method with each set of parameters provided by the data source.
  For more complex scenarios, you can also use external data sources like CSV files, [databases](../D/database.md), or XML files. You would need to write a method that reads the data and converts it into `TestCaseData` objects.
  Remember to keep your data source maintainable and easy to understand, as complex data sources can make your tests harder to read and debug.

#### What is the role of TestFixture in NUnit?

  In [NUnit](../N/nunit.md), a **TestFixture** is an attribute that marks a class as containing tests and, optionally, [setup](../S/setup.md) or teardown methods. It serves as a container for a set of related tests and allows for any initialization or cleanup code to be run before or after the tests are executed.
  Here's an example of a TestFixture:

  ```
  [TestFixture]
  public class CalculatorTests
  {
      private Calculator _calculator;
      [SetUp]
      public void Init()
      {
          // This code runs before each test
          _calculator = new Calculator();
      }
      [TearDown]
      public void Cleanup()
      {
          // This code runs after each test
          _calculator = null;
      }
      [Test]
      public void Add_WhenCalled_ReturnsSum()
      {
          // Arrange is done in SetUp
          // Act
          int result = _calculator.Add(1, 2);
          // Assert
          Assert.AreEqual(3, result);
      }
      // More tests...
  }
  ```
  Using **TestFixture**, you can:

  - Group tests logically.
  - Share setup and cleanup code across multiple tests, reducing redundancy.
  - Apply a common context to a set of tests, which is especially useful in data-driven testing.
  **TestFixture** can also take parameters, allowing for the same set of tests to be run with different inputs, facilitating [parameterized testing](../P/parameterized-testing.md). This is particularly useful when you want to test the same logic under various conditions.

  - Group tests logically.
  - Share setup and cleanup code across multiple tests, reducing redundancy.
  - Apply a common context to a set of tests, which is especially useful in data-driven testing.

#### How can you integrate NUnit with other tools like Selenium for e2e testing?

  Integrating **[NUnit](../N/nunit.md)** with **[Selenium](../S/selenium.md)** for end-to-end (e2e) testing involves using [NUnit](../N/nunit.md) as the [test runner](../T/test-runner.md) and [Selenium](../S/selenium.md) for browser automation. Here's a concise guide to achieve this integration:

  1. **Reference [Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)**: Ensure your project references the [Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md). This can be done via NuGet package manager.

    ```
    Install-Package Selenium.WebDriver
    ```

  2. **Create [Test Cases](../T/test-case.md)**: Write [test cases](../T/test-case.md) using [NUnit](../N/nunit.md)'s annotations. Use [Selenium](../S/selenium.md) [API](../A/api.md) to interact with the web browser within these tests.

    ```
    [TestFixture]
    public class SeleniumTests
    {
        private IWebDriver driver;
        [SetUp]
        public void SetUp()
        {
            // Initialize WebDriver, e.g., ChromeDriver
            driver = new ChromeDriver();
        }
        [Test]
        public void TestExample()
        {
            // Use Selenium to navigate and interact with the browser
            driver.Navigate().GoToUrl("http://example.com");
            Assert.IsTrue(driver.Title.Contains("Example Domain"));
        }
        [TearDown]
        public void TearDown()
        {
            // Cleanup: Close the browser after each test
            driver.Quit();
        }
    }
    ```

  3. **Run Tests**: Execute the tests using [NUnit](../N/nunit.md)'s [test runner](../T/test-runner.md). This can be done through the command line, a Continuous Integration (CI) server, or an IDE that supports [NUnit](../N/nunit.md).
  By following these steps, you can leverage [NUnit](../N/nunit.md)'s testing capabilities with [Selenium](../S/selenium.md)'s browser automation to create robust e2e tests. Remember to manage [WebDriver](../W/webdriver.md) instances properly to avoid resource leaks, and consider using the `TearDown` attribute to close browsers after tests complete.

  1. **Reference [Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)**: Ensure your project references the [Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md). This can be done via NuGet package manager.

    ```
    Install-Package Selenium.WebDriver
    ```

  2. **Create [Test Cases](../T/test-case.md)**: Write [test cases](../T/test-case.md) using [NUnit](../N/nunit.md)'s annotations. Use [Selenium](../S/selenium.md) [API](../A/api.md) to interact with the web browser within these tests.

    ```
    [TestFixture]
    public class SeleniumTests
    {
        private IWebDriver driver;
        [SetUp]
        public void SetUp()
        {
            // Initialize WebDriver, e.g., ChromeDriver
            driver = new ChromeDriver();
        }
        [Test]
        public void TestExample()
        {
            // Use Selenium to navigate and interact with the browser
            driver.Navigate().GoToUrl("http://example.com");
            Assert.IsTrue(driver.Title.Contains("Example Domain"));
        }
        [TearDown]
        public void TearDown()
        {
            // Cleanup: Close the browser after each test
            driver.Quit();
        }
    }
    ```

  3. **Run Tests**: Execute the tests using [NUnit](../N/nunit.md)'s [test runner](../T/test-runner.md). This can be done through the command line, a Continuous Integration (CI) server, or an IDE that supports [NUnit](../N/nunit.md).
