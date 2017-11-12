// @flow

import chroma from "chroma-js";

export const black = "hsl(0, 0%, 4%)";
export const blackBis = "hsl(0, 0%, 7%)";
export const blackTer = "hsl(0, 0%, 14%)";

export const greyDarker = "hsl(0, 0%, 21%)";
export const greyDark = "hsl(0, 0%, 29%)";
export const grey = "hsl(0, 0%, 48%)";
export const greyLight = "hsl(0, 0%, 71%)";
export const greyLighter = "hsl(0, 0%, 86%)";

export const whiteTer = "hsl(0, 0%, 96%)";
export const whiteBis = "hsl(0, 0%, 98%)";
export const white = "hsl(0, 0%, 100%)";

export const orange = "hsl(14,  100%, 53%)";
export const yellow = "hsl(48,  100%, 67%)";
export const green = "hsl(141, 71%,  48%)";
export const turquoise = "hsl(171, 100%, 41%)";
export const cyan = "hsl(204, 86%,  53%)";
export const blue = "hsl(217, 71%,  53%)";
export const purple = "hsl(271, 100%, 71%)";
export const red = "hsl(348, 100%, 61%)";

// ---------------//
// Derived colors //
// ---------------//

export const primary = turquoise;

export const info = cyan;
export const success = green;
export const warning = yellow;
export const danger = red;

export const light = whiteTer;
export const dark = greyDarker;

const findColorInvert = color => {
  const c = chroma(color);
  const luminance = c.luminance;

  if (luminance > 0.55) {
    return "rgba(0, 0, 0, 0.7)";
  } else {
    return "#fff";
  }
};

export const orangeInvert = findColorInvert(orange);
export const yellowInvert = findColorInvert(yellow);
export const greenInvert = findColorInvert(green);
export const turquoiseInvert = findColorInvert(turquoise);
export const cyanInvert = findColorInvert(cyan);
export const blueInvert = findColorInvert(blue);
export const purpleInvert = findColorInvert(purple);
export const redInvert = findColorInvert(red);

export const primaryInvert = turquoiseInvert;
export const infoInvert = cyanInvert;
export const successInvert = greenInvert;
export const warningInvert = yellowInvert;
export const dangerInvert = redInvert;
export const lightInvert = dark;
export const darkInvert = light;

// General colors

export const background = whiteTer;

export const border = greyLighter;
export const borderHover = greyLight;

// Text colors

export const text = greyDark;
export const textInvert = findColorInvert(text);
export const textLight = grey;
export const textStrong = greyDarker;

// Code colors

export const code = red;
export const codeBackground = background;

export const pre = text;
export const preBackground = background;

// Link colors

export const link = blue;
export const linkInvert = blueInvert;
export const linkVisited = purple;

export const linkHover = greyDarker;
export const linkHoverBorder = greyLight;

export const linkFocus = greyDarker;
export const linkFocusBorder = blue;

export const linkActive = greyDarker;
export const linkActiveBorder = greyDark;

export const colors = {
  white: [white, black],
  black: [black, white],
  light: [light, lightInvert],
  dark: [dark, darkInvert],
  primary: [primary, primaryInvert],
  link: [link, linkInvert],
  info: [info, infoInvert],
  success: [success, successInvert],
  warning: [warning, warningInvert],
  danger: [danger, dangerInvert]
};
