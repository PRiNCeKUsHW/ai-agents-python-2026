// Course design system: "Agent Console". See COURSE_DESIGN_SYSTEM.md before changing anything here.
export const W = 1920;
export const H = 1080;

// "Paper" light theme (Modules 1-6): warm off-white page, dark ink, deeper accents for contrast
const PAPER = {
  ink: "#F7F4EC", // page
  ink2: "#EFEBE0",
  surface: "#FFFFFF",
  surface2: "#F4F1E8",
  line: "#DDD6C6",
  text: "#1E2330",
  muted: "#555D6E",
  faint: "#8C93A1",
  teal: "#0B8A68", // primary: the agent / success / "correct"
  amber: "#B86E00", // attention: highlights, warnings, numbers
  blue: "#2B66D1", // information, data flow
  violet: "#7347C9", // the model / LLM
  coral: "#CC3348", // errors, wrong answers
  code: "#FFFEFA", // code + terminal panels
  codeHead: "#F3EFE4",
  codeText: "#2A2F3A",
  shadow: "rgba(60,48,20,0.10)",
};

// One theme per module, chosen to fit what the module teaches (rule from 2026-11-17).
// Module 0 "Terminal Night": the dark look of a terminal and a GitHub page, because the module is
// about the terminal, virtual environments and Git. Green = success / the prompt, orange = Git.
const TERMINAL_NIGHT: typeof PAPER = {
  ink: "#0D1117",
  ink2: "#10161E",
  surface: "#161B22",
  surface2: "#1C2330",
  line: "#30363D",
  text: "#E6EDF3",
  muted: "#9DA7B3",
  faint: "#6E7681",
  teal: "#3FB950", // success, the shell prompt, "correct"
  amber: "#F0883E", // Git orange: highlights, commits, numbers
  blue: "#58A6FF", // information, paths, data flow
  violet: "#BC8CFF", // GitHub / remote
  coral: "#FF7B72", // errors, wrong answers
  code: "#0B0F14",
  codeHead: "#161B22",
  codeText: "#E6EDF3",
  shadow: "rgba(0,0,0,0.45)",
};

const SYNTAX_PAPER: Record<string, string> = {
  kw: "#A626A4",
  con: "#986801",
  str: "#3E8E3A",
  num: "#986801",
  com: "#8E929B",
  fn: "#2F6FE0",
  cls: "#B35C00",
  bi: "#0F7FA6",
  dec: "#D1453B",
  op: "#3B4252",
  pun: "#5A6070",
  "": "#2A2F3A",
};

const SYNTAX_NIGHT: Record<string, string> = {
  kw: "#FF7B72",
  con: "#79C0FF",
  str: "#A5D6FF",
  num: "#79C0FF",
  com: "#8B949E",
  fn: "#D2A8FF",
  cls: "#FFA657",
  bi: "#79C0FF",
  dec: "#FFA657",
  op: "#E6EDF3",
  pun: "#C9D1D9",
  "": "#E6EDF3",
};

export const THEMES: Record<number, { name: string; colors: typeof PAPER; syntax: Record<string, string> }> = {
  0: { name: "Terminal Night", colors: TERMINAL_NIGHT, syntax: SYNTAX_NIGHT },
};
const DEFAULT_THEME = { name: "Paper", colors: PAPER, syntax: SYNTAX_PAPER };

// Live colours. Every component reads C / SYNTAX while rendering, so applyTheme() at the top of a
// composition switches the whole video.
export const C = { ...PAPER };
export const SYNTAX: Record<string, string> = { ...SYNTAX_PAPER };
export const applyTheme = (module: number) => {
  const t = THEMES[module] ?? DEFAULT_THEME;
  Object.assign(C, t.colors);
  Object.keys(SYNTAX).forEach((k) => delete SYNTAX[k]);
  Object.assign(SYNTAX, t.syntax);
  return t.name;
};

/** "#RRGGBB" + alpha -> rgba(), so tints follow the theme. */
export const alpha = (hex: string, a: number) =>
  `rgba(${parseInt(hex.slice(1, 3), 16)},${parseInt(hex.slice(3, 5), 16)},${parseInt(hex.slice(5, 7), 16)},${a})`;

export type Tone = "teal" | "amber" | "blue" | "violet" | "coral" | "muted";
export const tone = (t?: string) => (C as Record<string, string>)[t ?? "teal"] ?? C.teal;

export const FONT = "Inter, 'Inter Display', system-ui, sans-serif";
export const MONO = "'JetBrains Mono', 'DejaVu Sans Mono', monospace";

export const SAFE = { x: 96, top: 132, bottom: 950 }; // content box; header above, footer below
export const CONTENT_W = W - SAFE.x * 2;
