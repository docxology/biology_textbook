import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { parseMermaid, renderMermaidSVG } from 'beautiful-mermaid';

const directory = process.argv[2];
const palette = {
  bg: '#ffffff', fg: '#000000', _text: '#000000', '_text-sec': '#666666',
  '_text-muted': '#999999', '_text-faint': '#bfbfbf', _line: '#808080',
  _arrow: '#262626', '_node-fill': '#f7f7f7', '_node-stroke': '#cccccc',
  '_group-fill': '#ffffff', '_group-hdr': '#f2f2f2', '_inner-stroke': '#e0e0e0',
  '_key-badge': '#e6e6e6',
};

for (const file of (await readdir(directory)).filter(file => file.endsWith('.mmd')).sort()) {
  const source = await readFile(join(directory, file), 'utf8');
  const { direction, subgraphs } = parseMermaid(source);
  const svg = (await renderMermaidSVG(source, { bg: 'white', fg: 'black' }))
    .replace(/ style="--bg:[^"]+"/, '')
    .replace(/<style>[\s\S]*?<\/style>/, '<style>text { font-family: "DejaVu Sans", sans-serif; }</style>')
    .replace(/var\(--([\w-]+)\)/g, (_, key) => {
      if (!(key in palette)) throw new Error(`Unknown SVG palette variable: ${key}`);
      return palette[key];
    });
  if (/@import|https?:\/\/(?!www\.w3\.org\/2000\/svg)|var\(/.test(svg)) {
    throw new Error(`Unexpected external reference or unresolved CSS in ${file}`);
  }
  const stem = join(directory, file.slice(0, -4));
  await writeFile(stem + '.svg', svg);
  await writeFile(stem + '.json', JSON.stringify({ direction, subgraphs }));
}
