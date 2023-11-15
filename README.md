# Pono Dev Tools

`pono-dev-tools` is a comprehensive automation suite designed to streamline the setup process of development environments on both Ubuntu and macOS systems. This project provides a Python script that automates the installation of essential development tools and configurations, saving valuable time and ensuring a consistent setup across multiple machines.

## Features

- **Automated Tool Installation:** Installs a curated list of development tools including iTerm2 (macOS), Oh My Zsh, Starship prompt, and SCM Breeze.
- **Configuration Management:** Sets up your custom `.zshrc`, Git configuration, and a collection of useful aliases.
- **Global Git Hooks:** Implements global Git hooks for consistent commit message formats across all your repositories.
- **Zsh Plugin Support:** Installs and configures `zsh-autosuggestions` and `zsh-syntax-highlighting` plugins.
- **GitHub Actions Integration:** Includes a GitHub Actions workflow for testing the installation and setup processes in a CI/CD environment.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system. Other dependencies, like `curl` and `git`, will be checked and installed by the script.

### Installation

1. **Clone the Repository or Copy the Project:**

   ```bash
    git clone https://github.com/embeddedadam/pono-dev-tools.git
    ```

2. **Run the Installation Script:**

    ```bash
    cd pono-dev-tools
    python3 install.py
    ```

### Customization

You can tailor the pono-dev-tools to fit your specific needs:
    1. Modify the install.py script and the files in the configs and aliases directories to suit your preferences.
    2. Update the .gitconfig and .zshrc files as needed to match your personal setup.

### How It Saves Development Time

The pono-dev-tools suite is designed to enhance productivity by:

- **Rapid Environment Setup:** Quickly configuring a new development environment with all your preferred tools and settings.
- **Consistency Across Environments:** Maintaining uniformity in development setups across different machines or among team members.
- **Ease of Updates and Maintenance:** Simplifying the process of modifying your development environment, with centralized updates and management.
- **Automated Testing Assurance:** Providing confidence in the setup process through integrated testing with GitHub Actions.

### Contributing

We welcome contributions to the pono-dev-tools project. If you're interested in contributing, please read our contribution guidelines for more information on how to get started.

### License

pono-dev-tools is made available under the Apache License. For more details, see the LICENSE file in the repository.
