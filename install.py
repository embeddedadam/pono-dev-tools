import os
import subprocess
import sys
import shutil
import logging
from pathlib import Path
from typing import List
from subprocess import CalledProcessError

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def run_subprocess(command: List[str]) -> None:
    try:
        subprocess.run(command, check=True, capture_output=False)
    except CalledProcessError as e:
        logging.error(f"Failed to run command {' '.join(command)}: {e}")


def install_prerequisites() -> None:
    logging.info("Installing prerequisites: curl and git.")
    run_subprocess(["which", "curl"])
    run_subprocess(["sudo", "apt-get", "install", "-y", "curl"])
    run_subprocess(["which", "git"])
    run_subprocess(["sudo", "apt-get", "install", "-y", "git"])


def install_iTerm2() -> None:
    if sys.platform == "darwin":
        logging.info("Installing iTerm2.")
        run_subprocess(["brew", "install", "--cask", "iterm2"])


def install_oh_my_zsh() -> None:
    logging.info("Installing Oh My Zsh.")
    run_subprocess(
            ["sh", "-c", "curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh"])


def install_starship() -> None:
    logging.info("Installing Starship.")
    try:
        run_subprocess(["bash", "-c", "curl -fsSL https://starship.rs/install.sh | sh"])
    except CalledProcessError as e:
        logging.error(f"Failed to install Starship: {e}")
        sys.exit(1)


def install_scm_breeze() -> None:
    logging.info("Installing SCM Breeze.")
    home_dir = str(Path.home())
    scm_breeze_dir = Path(home_dir) / ".scm_breeze"
    if not scm_breeze_dir.exists():
        run_subprocess(["git", "clone", "https://github.com/scmbreeze/scm_breeze.git", str(scm_breeze_dir)])
    if scm_breeze_dir.exists():
        run_subprocess([str(scm_breeze_dir / "install.sh")])
    else:
        logging.error("Failed to clone SCM Breeze repository.")


def copy_configs() -> None:
    logging.info("Copying configuration files.")
    config_dir: Path = Path(__file__).parent / "configs"
    home_dir: Path = Path.home()
    for config in config_dir.glob("*"):
        logging.info(f"Copying {config.name} to {home_dir / f'{config.name}'}")
        shutil.copy(config, home_dir / f"{config.name}")


def setup_aliases() -> None:
    logging.info("Setting up aliases.")
    with open(Path(__file__).parent / "aliases/my-aliases.sh", "r") as aliases_file:
        aliases_content: str = aliases_file.read()
    with open(Path.home() / ".zshrc", "a") as zshrc_file:
        zshrc_file.write("\n" + aliases_content)


def setup_global_git_hooks() -> None:
    logging.info("Setting up global Git hooks.")
    hook_dir: Path = Path.home() / ".git_hooks"
    hook_dir.mkdir(exist_ok=True)
    shutil.copy(Path(__file__).parent / "configs" / "commit-msg", hook_dir / "commit-msg")
    run_subprocess(["git", "config", "--global",
                   "core.hooksPath", str(hook_dir)])


def install_zsh_autosuggestions() -> None:
    logging.info("Installing Zsh Autosuggestions.")
    autosuggestions_dir: Path = Path.home(
    ) / ".oh-my-zsh/custom/plugins/zsh-autosuggestions"
    if not autosuggestions_dir.exists():
        run_subprocess(
            ["git", "clone", "https://github.com/zsh-users/zsh-autosuggestions", str(autosuggestions_dir)])


def install_zsh_syntax_highlighting() -> None:
    logging.info("Installing Zsh Syntax Highlighting.")
    syntax_highlighting_dir: Path = Path.home(
    ) / ".oh-my-zsh/custom/plugins/zsh-syntax-highlighting"
    if not syntax_highlighting_dir.exists():
        run_subprocess(
            ["git", "clone", "https://github.com/zsh-users/zsh-syntax-highlighting", str(syntax_highlighting_dir)])


def update_zshrc_plugins() -> None:
    logging.info("Updating .zshrc with new plugins.")
    zshrc_path = "~/.zshrc"
    expanded_path = os.path.expanduser(zshrc_path)

    # Define the plugins to add
    plugins_to_add = ['zsh-autosuggestions', 'zsh-syntax-highlighting']

    # Read the existing .zshrc content
    with open(expanded_path, 'r') as file:
        lines = file.readlines()

    # Check and add each plugin if not already present
    for plugin in plugins_to_add:
        plugin_str = f"plugins+=({plugin})"
        if not any(plugin_str in line for line in lines):
            # Add the plugin to the plugins list in the file
            lines = [line.replace('plugins=(', f'plugins=({plugin} ') if 'plugins=(' in line else line for line in lines]

    # Write the updated content back to .zshrc
    with open(expanded_path, 'w') as file:
        file.writelines(lines)


def main() -> None:
    logging.info("Starting installation process.")
    install_prerequisites()
    install_iTerm2()
    install_oh_my_zsh()
    install_starship()
    install_scm_breeze()
    copy_configs()
    setup_aliases()
    setup_global_git_hooks()
    install_zsh_autosuggestions()
    install_zsh_syntax_highlighting()
    update_zshrc_plugins()
    logging.info("Installation process completed.")


if __name__ == "__main__":
    main()
