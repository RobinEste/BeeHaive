import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [
    mdx(),
    react(),
    tailwind(),
  ],
  output: 'static',
  server: {
    port: 4321,
  },
  vite: {
    envPrefix: 'PUBLIC_',
  },
});
