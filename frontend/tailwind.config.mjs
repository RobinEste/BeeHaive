/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './src/**/*.{astro,html,js,jsx,ts,tsx,mdx}',
  ],
  theme: {
    extend: {
      // ── BRAND COLORS ──────────────────────────────
      colors: {
        teal: {
          DEFAULT: '#44C2BA',
          light:   '#8BE6DA',
        },
        gold: {
          DEFAULT: '#E9CA62',
          yellow:  '#EEDB43',
        },
        bg: {
          DEFAULT: '#0C1E1D',
          2:       '#122C2A',
          3:       '#163330',
        },
        content: {
          DEFAULT: '#E0F2F1',
          dim:     'rgba(224,242,241,0.62)',
          muted:   'rgba(224,242,241,0.36)',
        },
      },

      // ── TYPOGRAPHY ────────────────────────────────
      fontFamily: {
        sans:  ['Space Grotesk', 'sans-serif'],
        mono:  ['Space Mono', 'monospace'],
      },
      fontSize: {
        'display-xl': ['clamp(3rem,6vw,6.5rem)', { lineHeight: '1.0',  letterSpacing: '-0.04em' }],
        'display-lg': ['clamp(2.2rem,3.8vw,3.5rem)', { lineHeight: '1.12', letterSpacing: '-0.03em' }],
        'display-md': ['clamp(1.8rem,2.5vw,2.4rem)', { lineHeight: '1.15', letterSpacing: '-0.02em' }],
        'body-lg':    ['1.12rem', { lineHeight: '1.8' }],
        'body':       ['1rem',    { lineHeight: '1.78' }],
        'body-sm':    ['0.87rem', { lineHeight: '1.65' }],
        'label':      ['0.7rem',  { lineHeight: '1',   letterSpacing: '0.2em' }],
        'mono-sm':    ['0.72rem', { lineHeight: '1',   letterSpacing: '0.08em' }],
      },

      // ── SPACING ───────────────────────────────────
      spacing: {
        'section': '7rem',
        'section-sm': '5rem',
      },

      // ── BORDER RADIUS ─────────────────────────────
      borderRadius: {
        'card':   '14px',
        'btn':    '8px',
        'pill':   '100px',
        'badge':  '6px',
      },

      // ── BORDERS ───────────────────────────────────
      borderColor: {
        'subtle':  'rgba(68,194,186,0.18)',
        'medium':  'rgba(68,194,186,0.38)',
      },

      // ── BOX SHADOWS / GLOWS ───────────────────────
      boxShadow: {
        'teal-sm':  '0 4px 24px rgba(68,194,186,0.28)',
        'teal-md':  '0 0 30px rgba(68,194,186,0.45), 0 8px 30px rgba(68,194,186,0.2)',
        'teal-lg':  '0 0 40px rgba(68,194,186,0.55)',
        'gold-sm':  '0 4px 18px rgba(233,202,98,0.25)',
        'gold-md':  '0 0 28px rgba(233,202,98,0.5)',
      },

      // ── BACKGROUND GRADIENTS ─────────────────────
      backgroundImage: {
        'orb-teal':  'radial-gradient(circle, rgba(68,194,186,0.13) 0%, transparent 65%)',
        'orb-gold':  'radial-gradient(circle, rgba(233,202,98,0.08) 0%, transparent 65%)',
        'grid-subtle':
          'linear-gradient(rgba(68,194,186,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(68,194,186,0.03) 1px, transparent 1px)',
        'glow-bar':  'linear-gradient(90deg, #44C2BA, #8BE6DA, #E9CA62, #EEDB43, #44C2BA)',
        'card-cta':  'linear-gradient(135deg, rgba(68,194,186,0.13) 0%, rgba(139,230,218,0.06) 100%)',
      },
      backgroundSize: {
        'grid': '48px 48px',
        'glow': '300%',
      },

      // ── BACKDROP ──────────────────────────────────
      backdropBlur: {
        nav: '18px',
      },

      // ── TRANSITIONS ───────────────────────────────
      transitionDuration: {
        DEFAULT: '200ms',
        slow:    '400ms',
      },

      // ── ANIMATION ─────────────────────────────────
      keyframes: {
        fadeUp: {
          from: { opacity: '0', transform: 'translateY(24px)' },
          to:   { opacity: '1', transform: 'translateY(0)' },
        },
        lumPulse: {
          from: { opacity: '0.8', transform: 'scale(1)' },
          to:   { opacity: '1',   transform: 'scale(1.1)' },
        },
        blink: {
          '0%, 100%': { opacity: '1' },
          '50%':      { opacity: '0.3' },
        },
        flowGlow: {
          from: { backgroundPosition: '0%' },
          to:   { backgroundPosition: '100%' },
        },
        graphPulse: {
          '0%, 100%': { opacity: '0.85' },
          '50%':      { opacity: '1' },
        },
      },
      animation: {
        'fade-up':    'fadeUp 0.5s ease both',
        'lum-pulse':  'lumPulse 7s ease-in-out infinite alternate',
        'blink':      'blink 2s ease-in-out infinite',
        'flow-glow':  'flowGlow 5s ease-in-out infinite alternate',
        'graph-pulse':'graphPulse 4s ease-in-out infinite',
      },
    },
  },
  plugins: [],
};
