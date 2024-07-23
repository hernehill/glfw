name = "glfw"

version = "3.4.0.hh.1.0.0"

authors = [
    "Camilla Lowy",
]

description = """OpenGL library"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = []

private_build_requires = []

variants = []


def commands():
    env.REZ_GLFW_ROOT = "{root}"
    env.GLFW_ROOT = "{root}"
    env.GLFW_LOCATION = "{root}"
    env.GLFW_INCLUDE_DIR = "{root}/include"

    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.PKG_CONFIG_PATH.append("{root}/lib64/pkgconfig")


uuid = "repository.glfw"
