# default.nix
with (import <nixpkgs> {});
mkShell {
  buildInputs = [
    python311
    python311Packages.pyside6
    python311Packages.numpy
    python311Packages.opencv4
    python311Packages.pyzmq
    python311Packages.sympy
  ];
}


# also need to install nixgl, https://github.com/guibou/nixGL
# and nixGL python3 main.py
