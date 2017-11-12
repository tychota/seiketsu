// @flow

import * as breakpoints from "./breakpoints";
import * as colors from "./colors";
import * as misc from "./misc";
import * as typography from "./typography";

const Theme = {
  breakpoints,
  colors,
  misc,
  typography
};
export type ThemeType = typeof Theme;
export type ThemePropsType = { theme: ThemeType };
export default Theme;
