<!-- omit in toc -->
# Contributing to Depeche

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Write about it (blog, article, ...)
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

<!-- omit in toc -->
## Table of Contents

- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Your First Code Contribution](#your-first-code-contribution)
- [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
- [Commit Messages](#commit-messages)
- [Join The Project Team](#join-the-project-team)

## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation](https://depeche.readthedocs.io/latest/).

Before you ask a question, it is best to search for existing [Issues](https://github.com/tom65536/depeche/issues) and [Discussions](https://github.com/tom65536/depeche/discussions) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue or discussion. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/tom65536/depeche/issues/new).
- Assign the label [question](https://github.com/tom65536/depeche/labels/question) to the issue.
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (python, pytest, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.


## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project licence.

### Reporting Bugs

<!-- omit in toc -->
#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](https://depeche.readthedocs.io/latest/). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [issue tracker](https://github.com/tom65536/depeche/issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<!-- omit in toc -->
#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to peregrinus@planet.ms .

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/tom65536/depeche/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for Depeche, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->
#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://depeche.readthedocs.io/latest/) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/tom65536/depeche/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

<!-- omit in toc -->
#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/tom65536/depeche/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- **Explain why this enhancement would be useful** to most Depeche users. You may also want to point out the other projects that solved it better and which could serve as inspiration.


### Your First Code Contribution
In order to contribute code changes you need to [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the
repository and modify the forked repository, unless you are a [project member](#join-the-project-team).

This project builds using [`flit`](https://pypi.org/project/flit/).
For your local build environment we strongly recommend
to have [`flit`](https://pypi.org/project/flit/) and [`flitenv`](https://pypi.org/project/flitenv/) installed.

Some important checks, such as [`ruff`](https://pypi.org/project/ruff/) are included in our [`pre-commit`](https://pypi.org/project/pre-commit/) configuration.

Of course, your build environment also needs a [`git`](https://git-scm.com/) client and a recent [Python](https://www.python.org/) installation.

Assuming you use [`pip`](https://pip.pypa.io/en/stable/getting-started/)
for package installation, you should run
```sh
python -m pip install flit flitenv pre-commit
```

Next, inside the project directory of the [cloned](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) repository,
[install the pre-commit hook scripts](https://pre-commit.com/index.html#3-install-the-git-hook-scripts).
```sh
pre-commit install
```

Apply your modifications using your favourite editor or IDE.

Before you submit your pull request ensure the following
check list:

- **Keep the modifications to a minimum**
and **stay focussed to the scope** of the [pull request](https://docs.github.com/en/pull-requests)/issue you are trying to resolve. A huge change set is difficult to
understand for the reviewer, and your pull request may
be refused, which would be disappointing for both sides.
- Make sure the pull request states clearly what problem(s) it resolves and how it is solved.
- Write unit tests for all relevant routines, try to keep code coverage high.
- All formal checks must succeed.
   * Type Checker ([PyRight]()): `flitenv run type pyright`
   * Unit Tests ([PyTest]()): `flitenv run test pytest`
   * Pre-Commit
- Think twice before ignoring the warnings.
- Your fork must be ready to merge: [synchronize](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) it if necessary.


### Improving The Documentation
<!-- TODO
Updating, improving and correcting the documentation

-->

## Styleguides
### Commit Messages
Although not a strict requirement, we recommend
to use [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/)
messages.

### Indentation
Please, use the indentation style recommended by the
project's [EditorConfig](https://editorconfig.org/).

## Join The Project Team
<!-- TODO -->

<!-- omit in toc -->
## Attribution
This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!
