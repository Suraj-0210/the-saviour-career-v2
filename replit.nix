{ pkgs }: {
    deps = [
      pkgs.python310Packages.flask
      pkgs.cowsay
    ];
}