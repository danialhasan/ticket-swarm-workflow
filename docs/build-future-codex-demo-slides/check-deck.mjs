import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const deckPath = join(here, "index.html");
const html = await readFile(deckPath, "utf8");
const minReadableText = 24;

const styleBlocks = [...html.matchAll(/<style>([\s\S]*?)<\/style>/g)].map((match) => match[1]);
const css = styleBlocks.join("\n");
const failures = [];

if (!css.includes("--min-readable-text: 24px;")) {
  failures.push("Missing --min-readable-text: 24px token.");
}

if (!/body\.workbench-mode\s*{[\s\S]*?overflow-y:\s*auto;/m.test(css)) {
  failures.push("body.workbench-mode must set overflow-y: auto.");
}

if (!/body\.workbench-mode\s*{[\s\S]*?overflow-x:\s*hidden;/m.test(css)) {
  failures.push("body.workbench-mode must set overflow-x: hidden.");
}

const fontSizePattern = /font-size:\s*([0-9]*\.?[0-9]+)px/g;
for (const match of css.matchAll(fontSizePattern)) {
  const size = Number(match[1]);
  if (size < minReadableText) {
    failures.push(`font-size ${size}px is below ${minReadableText}px.`);
  }
}

const fontShorthandPattern = /font:\s*([0-9]*\.?[0-9]+)px\b/g;
for (const match of css.matchAll(fontShorthandPattern)) {
  const size = Number(match[1]);
  if (size < minReadableText) {
    failures.push(`font shorthand ${size}px is below ${minReadableText}px.`);
  }
}

const slideCount = (html.match(/<section class="slide\b/g) || []).length;
const notesCount = (html.match(/<aside class="notes">/g) || []).length;
if (slideCount === 0) {
  failures.push("No slides found.");
}

if (slideCount !== notesCount) {
  failures.push(`Slide count (${slideCount}) must match notes count (${notesCount}).`);
}

if (failures.length > 0) {
  console.error(failures.join("\n"));
  process.exit(1);
}

console.log(`Deck check passed: ${slideCount} slides, ${notesCount} notes, min font ${minReadableText}px.`);
