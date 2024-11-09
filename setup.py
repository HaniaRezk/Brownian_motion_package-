from setuptools import setup

setup(
    name="your_package_name",
    use_scm_version=True,  # Enable setuptools_scm
    setup_requires=["setuptools_scm"],  # Ensure setuptools_scm is available during setup
)
