import { useState, useEffect, useRef, useCallback } from 'react';

/* ── Types ── */
interface BB { code: string; name: string; explanation: string }

interface Step {
  id: string;
  label: string;
  subtitle: string;
  bbs: BB[];
  description: string;
  evalLoop: string;
  duration: number;
}

interface FlowTab {
  id: string;
  label: string;
  intro: string;
  steps: Step[];
}

/* ── Flow data per tab ── */
const TABS: FlowTab[] = [
  {
    id: 'waarom',
    label: 'Waarom?',
    intro: 'Hoe ontstond het idee voor de AI-Readiness Audit? Van observatie naar concreet product.',
    steps: [
      {
        id: 'ideation', label: 'Ideevorming',
        subtitle: 'Waarom falen implementaties van AI?',
        bbs: [
          { code: 'BB_01', name: 'Knowledge', explanation: 'Domein-, proces- en technische kennis uit het werkveld vormen de basis voor het herkennen van het probleem.' },
        ],
        description: 'Wij zagen het keer op keer gebeuren: organisaties starten vol enthousiasme met AI. Er komt een visiedocument, een pilot, soms zelfs een AI-strategie. En dan stopt het. De pilot haalt nooit productie. Het rapport belandt in een la. Niemand weet meer waarom het ook alweer een goed idee was. Dat intrigeerde ons: waar gaat het eigenlijk mis?',
        evalLoop: 'Hebben we het probleem scherp genoeg? Begrijpen we waarom het steeds opnieuw misgaat en bij welke organisaties?',
        duration: 16000,
      },
      {
        id: 'vragen', label: 'Vragen stellen',
        subtitle: 'Waar gaat het fout?',
        bbs: [
          { code: 'BB_04', name: 'Prompt Design', explanation: 'De vragen worden specifiek geformuleerd als prompts om juiste en correcte antwoorden te krijgen.' },
          { code: 'BB_06', name: 'Model Engines', explanation: 'AI-modellen hebben specifieke kwaliteiten. We maken bewuste keuzes voor de AI die vragen het beste kan beantwoorden.' },
        ],
        description: 'Dus gingen wij vragen stellen, onderzoek doen met behulp van AI, use-cases van succesverhalen en mislukkingen lezen.',
        evalLoop: 'Stellen we de juiste vragen? Kunnen we ze beter formuleren? Welk AI-model werkt het best?',
        duration: 16000,
      },
      {
        id: 'antwoorden', label: 'Antwoorden verzamelen',
        subtitle: 'Signalen ophalen en verbinden',
        bbs: [
          { code: 'BB_05', name: 'Tool Integration', explanation: 'AI gebruikt tools voor het lezen van websites en pdf\'s om data uit bronnen te kunnen analyseren.' },
          { code: 'BB_03', name: 'Dynamic Context', explanation: 'De antwoorden, use-cases en bronnen worden gestructureerd vastgelegd als doorzoekbare context. Zo bouw je een eigen kennisbank op.' },
        ],
        description: 'We kregen antwoorden over een directie die dacht klaar te zijn, maar de werkvloer niet meehad. Over teams die prachtige AI-tools bouwden op data die niet klopte. En over medewerkers die zich overvallen voelden door verandering van bovenaf.',
        evalLoop: 'Zijn onze bevindingen volledig? Hebben we alle problemen in kaart? Worden de juiste antwoorden uit de bronnen gehaald?',
        duration: 16000,
      },
      {
        id: 'beeldvorming', label: 'Beeldvorming',
        subtitle: 'Concreet productvoorstel opstellen',
        bbs: [
          { code: 'BB_02', name: 'Client Blueprint', explanation: 'Het idee word vastgelegd in onder andere een procesflow en product requirements. Let op: deze zal nog regelmatig worden aangepast gedurende het project (bijv. na review prototype).' },
        ],
        description: 'De traditionele manier om dit aan te pakken is een audit: je spreekt met een paar key players en doet onderzoek en koppelt terug. Probleem: duurt lang, is kostbaar en mist vaak draagvlak. Idee: de AI Readiness Audit. Gerichte vragen aan grote groepen medewerkers, vertrouwelijke verwerking, met readiness scores, concrete use cases en een geprioriteerde roadmap.',
        evalLoop: 'Is de Client Blueprint volledig genoeg om te gaan bouwen? Klopt onze tech-stack? Verstandig om eerst een prototype te maken?',
        duration: 16000,
      },
    ],
  },
  {
    id: 'hoe',
    label: 'Hoe?',
    intro: 'Hoe is de AI-Readiness Audit gebouwd? Het technische traject van ontwerp naar werkend product.',
    steps: [
      // Placeholder — Robin werkt dit later uit
      {
        id: 'placeholder-hoe', label: 'Binnenkort',
        subtitle: 'Het bouwproces wordt uitgewerkt',
        bbs: [],
        description: 'Dit onderdeel wordt binnenkort aangevuld met het technische traject: van blueprint naar werkend product, inclusief de FDE-iteratie, privacy-architectuur en teststraat.',
        evalLoop: '',
        duration: 10000,
      },
    ],
  },
  {
    id: 'wat',
    label: 'Wat?',
    intro: 'Wat levert de AI-Readiness Audit op? De deliverables en het resultaat.',
    steps: [
      // Placeholder — Robin werkt dit later uit
      {
        id: 'placeholder-wat', label: 'Binnenkort',
        subtitle: 'De deliverables worden uitgewerkt',
        bbs: [],
        description: 'Dit onderdeel wordt binnenkort aangevuld met de concrete deliverables: dashboard, rapport, deelnemersportaal en de analyse met human-in-the-loop.',
        evalLoop: '',
        duration: 10000,
      },
    ],
  },
];

/* ── Block Component ── */
function Block({ step, isActive, isVisible, onClick }: {
  step: Step; isActive: boolean; isVisible: boolean; onClick?: () => void;
}) {
  return (
    <div onClick={onClick} style={{
      background: isActive ? '#122C2A' : '#0F2322',
      border: `2px solid ${isActive ? '#44C2BA' : 'rgba(68, 194, 186, 0.25)'}`,
      borderRadius: '14px',
      padding: '16px 20px',
      width: 190,
      minWidth: 190,
      cursor: isVisible ? 'pointer' : 'default',
      opacity: isVisible ? 1 : 0,
      transform: isVisible ? 'translateY(0) scale(1)' : 'translateY(12px) scale(0.95)',
      transition: 'all 0.5s cubic-bezier(0.16, 1, 0.3, 1)',
      boxShadow: isActive ? '0 0 30px rgba(68, 194, 186, 0.2)' : 'none',
      position: 'relative',
    }}>
      {isActive && (
        <div style={{
          position: 'absolute', bottom: 0, left: 0, right: 0, height: '2px',
          background: 'linear-gradient(90deg, #44C2BA, #8BE6DA)',
          boxShadow: '0 0 12px #44C2BA',
        }} />
      )}
      <div style={{
        fontFamily: "'Space Grotesk', sans-serif", fontSize: '0.88rem',
        fontWeight: 600,
        color: isActive ? '#E0F2F1' : 'rgba(224, 242, 241, 0.9)',
        lineHeight: 1.3, marginBottom: '4px',
        transition: 'color 0.3s',
      }}>
        {step.label}
      </div>
      <div style={{
        fontFamily: "'Space Grotesk', sans-serif", fontSize: '0.68rem',
        color: isActive ? 'rgba(224, 242, 241, 0.72)' : 'rgba(224, 242, 241, 0.5)',
        lineHeight: 1.3, marginBottom: '8px',
        fontWeight: 300, fontStyle: 'italic',
        transition: 'color 0.3s',
      }}>
        {step.subtitle}
      </div>
      <div style={{
        display: 'flex', flexWrap: 'wrap', gap: '4px',
        opacity: isActive ? 1 : 0.5,
        transition: 'opacity 0.3s',
      }}>
        {step.bbs.map(bb => (
          <span key={bb.code} style={{
            fontFamily: "'Space Mono', monospace",
            fontSize: '0.72rem',
            letterSpacing: '0.06em',
            color: isActive ? '#E9CA62' : 'rgba(233, 202, 98, 0.5)',
            background: isActive ? 'rgba(233, 202, 98, 0.1)' : 'rgba(233, 202, 98, 0.04)',
            border: `1px solid ${isActive ? 'rgba(233, 202, 98, 0.25)' : 'rgba(233, 202, 98, 0.1)'}`,
            borderRadius: '3px',
            padding: '3px 8px',
            transition: 'color 0.3s, background 0.3s, border-color 0.3s',
          }}>
            {bb.name}
          </span>
        ))}
      </div>
    </div>
  );
}

/* ── Connector line ── */
function Connector({ isVisible }: { isVisible: boolean }) {
  return (
    <div style={{
      display: 'flex', alignItems: 'center', alignSelf: 'center',
      width: 48, minWidth: 48, justifyContent: 'center',
    }}>
      <div style={{
        height: '2px',
        width: isVisible ? '100%' : '0%',
        background: '#44C2BA',
        transition: 'width 0.4s ease-out',
        boxShadow: isVisible ? '0 0 8px rgba(68, 194, 186, 0.2)' : 'none',
        borderRadius: '1px',
      }} />
    </div>
  );
}

/* ── Description panel with eval loop ── */
function DescriptionPanel({ step }: { step: Step | null }) {
  if (!step) return null;

  return (
    <div style={{ padding: '1rem 0' }}>
      {/* Title */}
      <span style={{
        fontFamily: "'Space Grotesk', sans-serif", fontSize: '0.95rem',
        fontWeight: 600, color: '#E0F2F1',
        display: 'block', marginBottom: '0.3rem',
      }}>
        {step.label}
      </span>

      {/* Subtitle */}
      <div style={{
        fontFamily: "'Space Grotesk', sans-serif", fontSize: '0.88rem',
        color: '#44C2BA', fontWeight: 500, marginBottom: '0.7rem',
        fontStyle: 'italic',
      }}>
        {step.subtitle}
      </div>

      {/* Description */}
      <p style={{
        fontFamily: "'Space Grotesk', sans-serif", fontSize: '0.92rem',
        color: 'rgba(224, 242, 241, 0.9)',
        lineHeight: 1.7, fontWeight: 300, margin: 0,
        maxWidth: 640, marginBottom: (step.bbs.length > 0 || step.evalLoop) ? '1.2rem' : 0,
      }}>
        {step.description}
      </p>

      {/* Building Blocks with explanations */}
      {step.bbs.length > 0 && (
        <div style={{
          display: 'flex', flexDirection: 'column', gap: '0.7rem',
          maxWidth: 640, marginBottom: step.evalLoop ? '0.7rem' : 0,
        }}>
          {step.bbs.map(bb => (
            <div key={bb.code}>
              <span style={{
                fontFamily: "'Space Mono', monospace",
                fontSize: '0.72rem',
                letterSpacing: '0.06em',
                color: '#E9CA62',
                background: 'rgba(233, 202, 98, 0.1)',
                border: '1px solid rgba(233, 202, 98, 0.25)',
                borderRadius: '3px',
                padding: '3px 8px',
                display: 'inline-block',
                marginBottom: '0.35rem',
              }}>
                {bb.name}
              </span>
              <p style={{
                fontFamily: "'Space Grotesk', sans-serif", fontSize: '0.88rem',
                color: 'rgba(224, 242, 241, 0.72)',
                lineHeight: 1.6, fontWeight: 300,
                margin: 0,
              }}>
                {bb.explanation}
              </p>
            </div>
          ))}
        </div>
      )}

      {/* Evaluation Loop */}
      {step.evalLoop && (
        <div style={{ maxWidth: 640 }}>
          <span style={{
            fontFamily: "'Space Mono', monospace",
            fontSize: '0.72rem',
            letterSpacing: '0.06em',
            color: '#E9CA62',
            background: 'rgba(233, 202, 98, 0.1)',
            border: '1px solid rgba(233, 202, 98, 0.25)',
            borderRadius: '3px',
            padding: '3px 8px',
            display: 'inline-block',
            marginBottom: '0.35rem',
          }}>
            Evaluation Loop
          </span>
          <p style={{
            fontFamily: "'Space Grotesk', sans-serif", fontSize: '0.88rem',
            color: 'rgba(224, 242, 241, 0.72)',
            lineHeight: 1.6, fontWeight: 300, fontStyle: 'italic',
            margin: 0,
          }}>
            {step.evalLoop}
          </p>
        </div>
      )}
    </div>
  );
}

/* ── Progress bar ── */
function ProgressBar({ current, total, isPlaying }: { current: number; total: number; isPlaying: boolean }) {
  return (
    <div style={{ display: 'flex', gap: '4px', alignItems: 'center' }}>
      {Array.from({ length: total }).map((_, i) => (
        <div key={i} style={{
          height: 3,
          flex: i <= current ? 1 : 0.5,
          borderRadius: '2px',
          background: i < current
            ? 'rgba(68, 194, 186, 0.5)'
            : i === current ? '#44C2BA' : 'rgba(68, 194, 186, 0.12)',
          transition: 'all 0.4s',
          boxShadow: i === current && isPlaying ? '0 0 8px rgba(68, 194, 186, 0.4)' : 'none',
        }} />
      ))}
    </div>
  );
}

/* ── Tab button ── */
function TabButton({ label, isActive, onClick }: { label: string; isActive: boolean; onClick: () => void }) {
  return (
    <button onClick={onClick} style={{
      background: isActive ? 'rgba(68, 194, 186, 0.15)' : 'transparent',
      color: isActive ? '#44C2BA' : 'rgba(68, 194, 186, 0.65)',
      border: `1.5px solid ${isActive ? 'rgba(68, 194, 186, 0.5)' : 'rgba(68, 194, 186, 0.15)'}`,
      borderRadius: '8px',
      padding: '0.5rem 1.2rem',
      fontWeight: isActive ? 700 : 500,
      fontSize: '0.88rem',
      cursor: 'pointer',
      fontFamily: "'Space Grotesk', sans-serif",
      transition: 'all 0.3s',
      letterSpacing: '0.01em',
    }}>
      {label}
    </button>
  );
}

/* ── Main Component ── */
export default function AuditWorkflow() {
  const [activeTab, setActiveTab] = useState(0);
  const [currentIndex, setCurrentIndex] = useState(-1);
  const [isPlaying, setIsPlaying] = useState(false);
  const [focusIndex, setFocusIndex] = useState<number | null>(null);
  const scrollRef = useRef<HTMLDivElement>(null);
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const stepRefs = useRef<(HTMLDivElement | null)[]>([]);

  const flow = TABS[activeTab];
  const steps = flow.steps;
  const visibleSteps = currentIndex >= 0 ? currentIndex + 1 : 0;
  const displayIndex = focusIndex !== null ? focusIndex : currentIndex;
  const displayStep = displayIndex >= 0 && displayIndex < steps.length ? steps[displayIndex] : null;

  // Reset refs when tab changes
  useEffect(() => {
    stepRefs.current = steps.map(() => null);
  }, [steps]);

  const advanceStep = useCallback(() => {
    setCurrentIndex(prev => {
      const next = prev + 1;
      if (next >= steps.length) {
        setIsPlaying(false);
        return prev;
      }
      return next;
    });
  }, [steps.length]);

  // Auto-play timer
  useEffect(() => {
    if (isPlaying && currentIndex >= 0 && currentIndex < steps.length) {
      const step = steps[currentIndex];
      timerRef.current = setTimeout(() => {
        if (currentIndex < steps.length - 1) {
          advanceStep();
        } else {
          setIsPlaying(false);
        }
      }, step.duration);
    }
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, [isPlaying, currentIndex, steps, advanceStep]);

  // Scroll active block into view
  useEffect(() => {
    if (currentIndex >= 0 && stepRefs.current[currentIndex]) {
      requestAnimationFrame(() => {
        stepRefs.current[currentIndex]?.scrollIntoView({
          behavior: 'smooth',
          block: 'nearest',
          inline: 'center',
        });
      });
    }
  }, [currentIndex]);

  const handleTabChange = useCallback((tabIndex: number) => {
    setActiveTab(tabIndex);
    setCurrentIndex(-1);
    setFocusIndex(null);
    setIsPlaying(false);
    if (scrollRef.current) {
      scrollRef.current.scrollTo({ left: 0 });
    }
  }, []);

  const handleStartStop = useCallback(() => {
    if (isPlaying) {
      setIsPlaying(false);
    } else {
      if (currentIndex === -1 || currentIndex >= steps.length - 1) {
        setCurrentIndex(0);
        setFocusIndex(null);
        setIsPlaying(true);
        if (scrollRef.current) {
          scrollRef.current.scrollTo({ left: 0, behavior: 'smooth' });
        }
      } else {
        setFocusIndex(null);
        setIsPlaying(true);
      }
    }
  }, [isPlaying, currentIndex, steps.length]);

  const handleBlockClick = useCallback((index: number) => {
    if (index < visibleSteps) {
      setIsPlaying(false);
      setFocusIndex(prev => prev === index ? null : index);
    }
  }, [visibleSteps]);

  const handleReset = useCallback(() => {
    setIsPlaying(false);
    setCurrentIndex(-1);
    setFocusIndex(null);
    if (scrollRef.current) {
      scrollRef.current.scrollTo({ left: 0, behavior: 'smooth' });
    }
  }, []);

  return (
    <div style={{ width: '100%' }}>

      {/* Tab navigation */}
      <div style={{
        display: 'flex', gap: '0.5rem',
        marginBottom: '1.5rem',
      }}>
        {TABS.map((tab, i) => (
          <TabButton
            key={tab.id}
            label={tab.label}
            isActive={activeTab === i}
            onClick={() => handleTabChange(i)}
          />
        ))}
      </div>

      {/* Controls + progress */}
      <div style={{
        display: 'flex', alignItems: 'center', gap: '1rem',
        marginBottom: '1.5rem',
      }}>
        <button onClick={handleStartStop} style={{
          background: isPlaying ? 'transparent' : '#E9CA62',
          color: isPlaying ? '#E9CA62' : '#0C1E1D',
          border: isPlaying ? '1.5px solid rgba(233, 202, 98, 0.5)' : 'none',
          borderRadius: '8px',
          padding: '0.6rem 1.4rem',
          fontWeight: 700,
          fontSize: '0.85rem',
          cursor: 'pointer',
          fontFamily: "'Space Grotesk', sans-serif",
          transition: 'background 0.3s, color 0.3s, border-color 0.3s, box-shadow 0.3s',
          boxShadow: !isPlaying ? '0 4px 18px rgba(233, 202, 98, 0.25)' : 'none',
          minWidth: 120,
        }}>
          {isPlaying ? '⏸ Pauzeer' : currentIndex === -1 ? '▶ Start' : currentIndex >= steps.length - 1 ? '▶ Opnieuw' : '▶ Hervat'}
        </button>

        {currentIndex >= 0 && (
          <button onClick={handleReset} style={{
            background: 'transparent',
            color: 'rgba(224, 242, 241, 0.72)',
            border: '1px solid rgba(68, 194, 186, 0.2)',
            borderRadius: '6px',
            padding: '0.5rem 1rem',
            fontSize: '0.78rem',
            cursor: 'pointer',
            fontFamily: "'Space Grotesk', sans-serif",
            transition: 'border-color 0.3s, color 0.3s',
          }}>
            Reset
          </button>
        )}

        <div style={{ flex: 1 }}>
          {currentIndex >= 0 && (
            <ProgressBar current={currentIndex} total={steps.length} isPlaying={isPlaying} />
          )}
        </div>
      </div>

      {/* Flow container */}
      <div
        ref={scrollRef}
        style={{
          display: 'flex',
          overflowX: 'auto',
          overflowY: 'hidden',
          padding: '20px 10px',
          gap: '0px',
          minHeight: 200,
          scrollBehavior: 'smooth',
          scrollbarWidth: 'none',
          WebkitOverflowScrolling: 'touch',
          maskImage: 'linear-gradient(to right, transparent 0%, black 2%, black 95%, transparent 100%)',
          WebkitMaskImage: 'linear-gradient(to right, transparent 0%, black 2%, black 95%, transparent 100%)',
        }}
      >
        {steps.map((step, i) => {
          const isVisible = i < visibleSteps;
          const isActive = i === displayIndex;
          const showConnector = i > 0 && isVisible;

          return (
            <div key={step.id} ref={el => { stepRefs.current[i] = el; }} style={{ display: 'flex', alignItems: 'center' }}>
              {showConnector && <Connector isVisible={isVisible} />}
              <Block
                step={step}
                isActive={isActive}
                isVisible={isVisible}
                onClick={() => handleBlockClick(i)}
              />
            </div>
          );
        })}
        <div style={{ minWidth: 40, flexShrink: 0 }} />
      </div>

      {/* Description panel */}
      <div style={{
        borderTop: '1px solid rgba(68, 194, 186, 0.15)',
        marginTop: '0.5rem',
        minHeight: 120,
      }}>
        {displayStep ? (
          <DescriptionPanel step={displayStep} />
        ) : (
          <div style={{ padding: '1rem 0' }}>
            <p style={{
              fontFamily: "'Space Grotesk', sans-serif", fontSize: '0.92rem',
              color: 'rgba(224, 242, 241, 0.9)', lineHeight: 1.7, fontWeight: 300,
              margin: 0,
            }}>
              {flow.intro}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
