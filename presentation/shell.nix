{ pkgs ? import <nixpkgs> {} }:
let
  mytexlive = pkgs.texlive.combine {inherit (pkgs.texlive) scheme-medium pgf; };
in
  pkgs.mkShell {
    buildInputs = [ mytexlive ];
}
