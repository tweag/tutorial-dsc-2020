{ pkgs ? import <nixpkgs> {} }:
let
  mytexlive = pkgs.texlive.combine {inherit (pkgs.texlive) scheme-medium pgf enumitem pgfplots adjustbox collectbox; };
in
  pkgs.mkShell {
    buildInputs = [ mytexlive ];
}
