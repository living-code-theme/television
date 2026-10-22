# Application-owned, locked native screenshot environment. No model credentials are passed through.
{
  description = "Living Code television native screenshot environment";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/7fd4004d0511991fff3a0524856a9be09e28c5f0";
  outputs = { self, nixpkgs }: {
    devShells.x86_64-linux.default = let
      pkgs = import nixpkgs { system = "x86_64-linux"; config.allowUnfree = true; };
    in pkgs.mkShell {
      packages = with pkgs; [ television python3 git bash kitty xorg-server xdotool imagemagick dejavu_fonts ];
      CAPTURE_MESA = "${pkgs.mesa}";
      FONTCONFIG_FILE = pkgs.makeFontsConf { fontDirectories = [ pkgs.dejavu_fonts ]; };
    };
  };
}
