import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="OpenAI B2B Onboarding Strategy",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - OpenAI Brand Style (Minimal & Geometric - Accessible)
st.markdown("""
<style>
    .main {
        background: #FAFAFA;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid #E5E5E5;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #FFFFFF;
        border: 1px solid #E5E5E5;
        border-radius: 4px;
        padding: 10px 20px;
        font-weight: 500;
        color: #6B7280;
    }
    .stTabs [aria-selected="true"] {
        background: #1F2937;
        color: #FFFFFF;
        border: 1px solid #1F2937;
    }
    div[data-testid="stMetricValue"] {
        font-size: 32px;
        font-weight: 600;
        color: #FFFFFF;
    }
    .stage-card {
        padding: 20px;
        border-radius: 4px;
        border-left: 3px solid #1F2937;
        margin: 10px 0;
        background: #FFFFFF;
        border: 1px solid #E5E5E5;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style='background: #1F2937; 
            padding: 50px; border-radius: 0px; margin-bottom: 20px; margin-top: 20pm; text-align: center;
            border-bottom: 3px solid #374151;'>
    <h1 style='color: #FFFFFF; font-size: 48px; margin: 0; font-weight: 600;'>
        OpenAI B2B Onboarding
    </h1>
    <p style='color: #D1D5DB; font-size: 24px; margin-top: 10px; font-weight: 400;'>
        Data Architecture + Enterprise Customer Activation Strategy
    </p>
</div>
""", unsafe_allow_html=True)

# Create tabs
tabs = st.tabs(["Overview", "Architecture", "Playbooks", "Metrics", "Roadmap"])

# ========== OVERVIEW TAB ==========
with tabs[0]:
    st.header("Overview")

    st.markdown("""
    <div style='background: #F3F4F6; 
                padding: 20px; border-radius: 4px; margin-bottom: 20px; color: #1F2937;
                border-left: 3px solid #1F2937; border: 1px solid #E5E5E5;'>
        <p style='margin: 0; line-height: 1.6; color: #1F2937;'>
            A strategy for onboarding and activating B2B and enterprise customers within OpenAI's existing technology infrastructure, integrating a personalization stack and behavior-driven framework. 
            Based on publicly available information about OpenAI's current tech stack, this document provides a data-driven approach to customer lifecycle management that leverages Salesforce, Clay, and other modern lifecycle messaging platforms.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
       
    st.subheader("🎯 Key Objectives")
    
    objectives = [
        "Streamline enterprise customer onboarding with automated workflows",
        "Create unified customer data architecture across sales, product, and success teams",
        "Enable personalized engagement at scale using AI-powered enrichment",
        "Implement data-driven lifecycle messaging to increase product adoption"
    ]
    
    for obj in objectives:
        st.markdown(f"✅ {obj}")
    
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: #1F2937; 
                    padding: 30px; border-radius: 4px; color: white; text-align: left;
                    border: 2px solid #374151;'>
            <h3 style='margin: 0; color: white; font-weight: 600;'>The Challenge</h3>
            <p style='margin: 0; color: #D1D5DB; font-weight: 400;'>ChatGPT Enterprise/Team customers have different:
                    <ul>
                    <li>Entry points (developer-led trial vs. top-down executive purchase)</li>
                    <li>Use cases (coding, research, customer support, content creation, analysis)</li>
                    <li>Organizational maturity (AI-native startups vs. traditional enterprises)</li>
                    <li>Activation points (first API call, team invite, workspace setup, model switching)</li></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: #1F2937; 
                    padding: 30px; border-radius: 4px; color: white; text-align: center;
                    border: 2px solid #374151;'>
            <h3 style='margin: 0; color: white; font-weight: 600;'>Increase Adoption</h3>
            <h1 style='font-size: 64px; margin: 10px 0; color: white; font-weight: 700;'>35%</h1>
            <p style='margin: 0; color: #D1D5DB; font-weight: 400;'>Product usage improvement</p>
        </div>
        """, unsafe_allow_html=True)

    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
       <div style='background: #F3F4F6; padding: 20px; border-radius: 4px; border-left: 3px solid #000000;
                    border: 1px solid #E5E5E5;'>
            <h4 style='color: #000000; margin-top: 0; font-weight: 600;'>🗄️ Tech Stack Assumptions</h3>
        
        <div style='line-height: 1.8; color: #1F2937;'>
            <ul>
            <li>CRM: Salesforce with custom objects for usage data, health scores, account hierarchy</li>
            <li>Data warehouse: Events, product telemetry, user behavior already streaming in real-time</li>
            <li>Enrichment: Clay or similar for account intelligence, intent signals, persona mapping</li>
            <li>Messaging platforms: Email (SendGrid/Braze), in-app (custom), push or SMS capability</li>
            <li>Analytics: Segment, product analytics, cohort analysis tools operational</li>
            <li>Integration layer: APIs connecting ChatGPT usage data → CRM → messaging platforms</li>
            </ul>        
             
       </div>""", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: #F3F4F6; padding: 20px; border-radius: 4px; border-left: 3px solid #000000;
                    border: 1px solid #E5E5E5;'>
            <h4 style='color: #000000; margin-top: 0; font-weight: 600;'>✨ Enhanced Capabilities Assumed</h3>
            <p style='margin: 0; color: #1F2937; font-weight: 500; padding: 20px 0'>
                 Amplitude tracks every action, Hightouch activates campaigns instantly, and Clay enriches with firmographic data.</p>
    
        <div style='line-height: 1.8; color: #1F2937;'>
            ✓ Unified customer journey (Amplitude + Hightouch)<br>
            ✓ Product analytics integration (Amplitude)<br>
            ✓ Real-time data activation (Hightouch Reverse ETL)<br>
            ✓ AI-driven behavioral personalization<br>
            ✓ Triggered by real-time events and usage<br>
        </div>
        
        </div>""", unsafe_allow_html=True)

# ========== ARCHITECTURE TAB ==========
with tabs[1]:
    st.header("Interactive Data Architecture")
    st.markdown("**Click each stage below to explore the data flow in detail**")
    
    stages = [
        {
            "id": "1",
            "title": "Event Capture",
            "tools": "Segment + Google Tag Manager",
            "description": "Customer interactions across web properties, API usage, and product events are captured in real-time.",
            "details": [
                "Page views & click tracking",
                "API call monitoring",
                "Feature usage events",
                "Conversion tracking"
            ]
        },
        {
            "id": "2",
            "title": "Data Processing & Storage",
            "tools": "Kafka → PostgreSQL | S3 | Databricks",
            "description": "Events flow through stream processing, then land in storage and analytical layers.",
            "details": [
                "Real-time stream processing",
                "Structured data storage",
                "Long-term data archival",
                "ML & analytics pipelines"
            ]
        },
        {
            "id": "3",
            "title": "Product Analytics",
            "tools": "Amplitude",
            "description": "Deep product usage analysis and behavioral cohort creation for B2B segmentation.",
            "details": [
                "API usage pattern analysis",
                "Team-level adoption tracking",
                "Feature engagement metrics",
                "Predictive churn indicators"
            ]
        },
        {
            "id": "4",
            "title": "Data Enrichment",
            "tools": "Clay (Claygent)",
            "description": "AI-powered enrichment adds firmographic data, technographic signals, and competitive intelligence.",
            "details": [
                "Company size & industry data",
                "Technology stack analysis",
                "Hiring pattern signals",
                "Decision maker identification"
            ]
        },
        {
            "id": "5",
            "title": "Reverse ETL & Activation",
            "tools": "Hightouch",
            "description": "Syncs enriched warehouse data to operational tools, turning insights into action across all platforms.",
            "details": [
                "Warehouse → CRM sync",
                "Behavioral segments distribution",
                "Health scores propagation",
                "Real-time data activation"
            ]
        },
        {
            "id": "6",
            "title": "CRM & Sales Enablement",
            "tools": "Salesforce",
            "description": "Unified customer view with product usage data enables data-driven account prioritization and health monitoring.",
            "details": [
                "360° customer profiles",
                "Usage-driven health scores",
                "Expansion opportunity detection",
                "Account prioritization"
            ]
        },
        {
            "id": "7",
            "title": "Lifecycle Messaging",
            "tools": "SendGrid | Braze | Iterable",
            "description": "Personalized messaging activates based on product usage, behavioral triggers, and predictive models.",
            "details": [
                "Usage-triggered campaigns",
                "Behavioral automation",
                "Milestone celebrations",
                "Predictive engagement"
            ]
        }
    ]
    
    for i, stage in enumerate(stages):
        with st.expander(f"**Stage {stage['id']}: {stage['title']}** - {stage['tools']}", expanded=(i==0)):
            st.markdown(f"""
          
                <p style='font-size: 16px; margin-bottom: 15px;'>{stage['description']}</p>
                <p style='font-size: 16px; margin-bottom: 10px;'>🔑 Key Capabilities:</p>
        
            """, unsafe_allow_html=True)
            
            cols = st.columns(2)
            for idx, detail in enumerate(stage['details']):
                with cols[idx % 2]:
                    st.markdown(f"✓ {detail}")
        
        if i < len(stages) - 1:
            st.markdown("<div style='text-align: center; font-size: 32px; color: #3b82f6;'>⬇️</div>", 
                       unsafe_allow_html=True)

# ========== PLAYBOOKS TAB ==========
with tabs[2]:
    st.header("Activation Playbooks")
    st.markdown("""
     <p style='margin: 0; line-height: 1.6; padding: 10px 0;'> Primary triggers are behavioral. Time-based fallbacks (marked with ⚠️) 
            only activate when customers do not exhibit expected behaviors, ensuring no one falls through the cracks.
           </p>
            <p style='margin: 0; line-height: 1.6; padding: 10px 0;'> 
                Three personas 
           </p>
    """, unsafe_allow_html=True)
            
    playbook_selection = st.selectbox(
        "Select a playbook to explore detailed behavioral triggers:",
        ["Developer-Led Growth 💻", "Executive Sponsorship 👔", "Multi-Team Expansion 🚀"]
    )
    
    if "Developer" in playbook_selection:
        st.markdown("""
        <div style='background: #1F2937; 
                    padding: 25px; border-radius: 4px; color: white; margin-bottom: 20px;
                    border: 2px solid #374151;'>
            <h2 style='color: white; margin: 0; font-weight: 600;'>💻 Developer-Led Growth (Behavior-Driven)</h2>
            <p style='color: #D1D5DB; margin-top: 10px; font-weight: 400;'>Target: Technical buyers and development teams</p>
            <p style='color: #9CA3AF; margin-top: 5px; font-size: 14px;'>⚡ Powered by Amplitude behavioral triggers + Hightouch activation</p>
        </div>
        """, unsafe_allow_html=True)
        
        timeline_df = pd.DataFrame({
            "Behavior Trigger": [
                "Account Created",
                "First API Call",
                "10+ Calls in 24hrs",
                "100+ Total API Calls",
                "Production Deployment",
                "⚠️ Fallback: 48hrs, 0 Calls"
            ],
            "Amplitude Signal": [
                "account.created event",
                "api.call event (first)",
                "Cohort: rapid_adopters",
                "Milestone: api_calls >= 100",
                "environment = production",
                "Cohort: inactive_48h"
            ],
            "Action": [
                "Welcome email + API keys & quickstart guide",
                "Congratulations message + advanced examples & tutorials",
                "Power user resources + optimization tips",
                "Milestone celebration + usage dashboard + office hours invite",
                "Executive ROI report + success story interview request",
                "Getting started assistance + technical support offer"
            ]
        })
        
        for idx, row in timeline_df.iterrows():
            is_fallback = "Fallback" in row['Behavior Trigger']
            border_color = "#1F2937" if is_fallback else "#1F2937"
            bg_color = "#FEFCE8" if is_fallback else "#FFFFFF"
            
            st.markdown(f"""
            <div style='background: {bg_color}; padding: 20px; border-radius: 4px; 
                        margin: 10px 0; border-left: 3px solid {border_color};
                        border: 1px solid #E5E5E5;'>
                <div style='margin-bottom: 10px;'>
                    <span style='background: {border_color}; color: white; padding: 6px 12px; 
                                border-radius: 2px; font-weight: 600; font-size: 13px;'>
                        {row['Behavior Trigger']}
                    </span>
                </div>
                <p style='color: #1F2937;'>📶 Amplitude: {row['Amplitude Signal']}</p>
                <p style='color: #1F2937;'>
                    <strong>▶️ Action:</strong> {row['Action']}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    elif "Executive" in playbook_selection:
        st.markdown("""
        <div style='background: #1F2937; 
                    padding: 25px; border-radius: 4px; color: white; margin-bottom: 20px;
                    border: 2px solid #374151;'>
            <h2 style='color: white; margin: 0; font-weight: 600;'>👔 Executive Sponsorship (Behavior-Driven)</h2>
            <p style='color: #D1D5DB; margin-top: 10px; font-weight: 400;'>Target: C-suite and VP-level decision makers</p>
            <p style='color: #9CA3AF; margin-top: 5px; font-size: 14px;'>⚡ Powered by Amplitude account-level analytics + Clay enrichment</p>
        </div>
        """, unsafe_allow_html=True)
        
        timeline_df = pd.DataFrame({
            "Behavior Trigger": [
                "Contract Signed",
                "Team Onboarded (5+ users)",
                "First Production Use",
                "Sustained Usage (30 days)",
                "Usage Plateau Detected",
                "⚠️ Fallback: Exec Dashboard Not Viewed"
            ],
            "Signal Source": [
                "Salesforce: contract.signed",
                "Amplitude: team_size >= 5",
                "Amplitude: production_workload.active",
                "Amplitude: active_days >= 30",
                "Amplitude: growth_rate = 0",
                "Amplitude: dashboard.viewed = false (14 days)"
            ],
            "Action": [
                "Personalized welcome from OpenAI executive + stakeholder mapping (Clay)",
                "Adoption dashboard shared + team usage metrics report",
                "ROI calculation email + success metrics + QBR invitation",
                "Executive briefing on business impact + innovation opportunities",
                "Innovation workshop offer + product roadmap preview",
                "Executive re-engagement campaign + CSM intervention"
            ]
        })
        
        for idx, row in timeline_df.iterrows():
            is_fallback = "Fallback" in row['Behavior Trigger']
            border_color = "#1F2937" if is_fallback else "#1F2937"
            bg_color = "#FEFCE8" if is_fallback else "#FFFFFF"
            
            st.markdown(f"""
            <div style='background: {bg_color}; padding: 20px; border-radius: 4px; 
                        margin: 10px 0; border-left: 3px solid {border_color};
                        border: 1px solid #E5E5E5;'>
                <div style='margin-bottom: 10px;'>
                    <span style='background: {border_color}; color: white; padding: 6px 12px; 
                                border-radius: 2px; font-weight: 600; font-size: 13px;'>
                        {row['Behavior Trigger']}
                    </span>
                </div>
                <p style='color: #1F2937;'>📶 Signal:</strong> {row['Signal Source']}
                </p>
                <p style='color: #1F2937;'>
                    <strong>▶️ Action:</strong> {row['Action']}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    else:  # Multi-Team Expansion
        st.markdown("""
        <div style='background: #1F2937; 
                    padding: 25px; border-radius: 4px; color: white; margin-bottom: 20px;
                    border: 2px solid #374151;'>
            <h2 style='color: white; margin: 0; font-weight: 600;'>🚀 Multi-Team Expansion (Behavior-Driven)</h2>
            <p style='color: #D1D5DB; margin-top: 10px; font-weight: 400;'>Target: Accounts with multiple departments or use cases</p>
            <p style='color: #9CA3AF; margin-top: 5px; font-size: 14px;'>⚡ Powered by Amplitude usage patterns + Clay stakeholder mapping</p>
        </div>
        """, unsafe_allow_html=True)
        
        timeline_df = pd.DataFrame({
            "Behavior Trigger": [
                "80% of Plan Capacity",
                "New Team Detected",
                "Cross-Department Usage",
                "Champion Behavior Detected",
                "New Stakeholder Hired",
                "⚠️ Fallback: Single Team or Department Only (90 days)"
            ],
            "Signal Source": [
                "Amplitude: usage / limit > 0.8",
                "Amplitude: new team_id detected",
                "Amplitude: team.count > 1",
                "Amplitude: engagement + advocacy score",
                "Clay: new VP/director hired at account",
                "Amplitude: team = 1 (90 days)"
            ],
            "Action": [
                "Upgrade conversation trigger + capacity planning call",
                "Cross-team introduction email + collaboration features",
                "Enterprise plan pitch + multi-team workshop invitation",
                "Reference program invitation + customer story interview",
                "Personalized outreach to new stakeholder + use case mapping",
                "Expansion discovery call + other stakeholder identification"
            ]
        })
        
        for idx, row in timeline_df.iterrows():
            is_fallback = "Fallback" in row['Behavior Trigger']
            border_color = "#1F2937" if is_fallback else "#1F2937"
            bg_color = "#FEFCE8" if is_fallback else "#FFFFFF"
            
            st.markdown(f"""
            <div style='background: {bg_color}; padding: 20px; border-radius: 4px; 
                        margin: 10px 0; border-left: 3px solid {border_color};
                        border: 1px solid #E5E5E5;'>
                <div style='margin-bottom: 10px;'>
                    <span style='background: {border_color}; color: white; padding: 6px 12px; 
                                border-radius: 2px; font-weight: 600; font-size: 13px;'>
                        {row['Behavior Trigger']}
                    </span>
                </div>
                 <p style='color: #1F2937;'>📶 Signal:</strong> {row['Signal Source']}
                </p>
                <p style='color: #1F2937;'>
                    <strong>▶️ Action:</strong> {row['Action']}
                </p>
            </div>
            """, unsafe_allow_html=True)

# ========== METRICS TAB ==========
with tabs[3]:
    st.header("Success Metrics & KPIs")
    
    st.subheader("Leading Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="⚡ Time to First API Call",
            value="< 24 hrs",
            delta="Target from contract signature"
        )
    
    with col2:
        st.metric(
            label="✅ Onboarding Completion",
            value="> 85%",
            delta="Within 14 days"
        )
    
    with col3:
        st.metric(
            label="📊 Product Qualified Leads",
            value="100+",
            delta="API calls in first 30 days"
        )
    
    with col4:
        st.metric(
            label="🌟 Activation Rate",
            value="40%",
            delta="First value event reached"
        )
    
    st.markdown("---")
    
    st.subheader("Business Outcomes")
    st.markdown("""
     <p style='margin: 0; line-height: 1.6; padding: 10px 0;'> Targets based on industry benchmarks (Gainsight, Pendo, KeyBanc) and implementation case studies (Hightouch,  Amplitude). 
                The following is a projected 12-month impact based on successful deployment and adoption.
           </p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: white; padding: 25px; border-radius: 4px; 
                    border: 2px solid #E5E5E5;'>
            <h4 style='color: #1F2937; margin-bottom: 20px; font-weight: 600; padding-bottom: 10px;'>Revenue & Growth Metrics</h4>
        """, unsafe_allow_html=True)
        
        metrics_df = pd.DataFrame({
            "Metric": ["Revenue Growth", "Customer LTV", "Time to Value"],
            "Target": ["+30%", "+20%", "-30%"],
            "Description": [
                "Expansion revenue increase",
                "LTV:CAC improvement",
                "Days to production deployment"
            ]
        })
        
        for _, row in metrics_df.iterrows():
            st.markdown(f"""
            <div style='padding: 15px; background: #F9FAFB; border-radius: 4px; margin: 10px 0;
                        border: 1px solid #E5E5E5;'>
                <div style='font-weight: 600; color: #1F2937;'>{row['Metric']}</div>
                <div style='font-size: 32px; font-weight: 700; color: #1F2937; margin: 5px 0;'>{row['Target']}</div>
                <div style='color: #64748b; font-size: 14px;'>{row['Description']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: white; padding: 25px; border-radius: 4px; 
                    border: 2px solid #E5E5E5;'>
            <h4 style='color: #1F2937; margin-bottom: 20px; font-weight: 600; padding-bottom: 10px;'>Customer Health & Retention</h4>
        """, unsafe_allow_html=True)
        
        health_df = pd.DataFrame({
            "Metric": ["Net Revenue Retention", "Customer Health Score", "Churn Reduction"],
            "Target": ["> 95%", "> 80%", "-20%"],
            "Description": [
                "At 12 months",
                "Accounts healthy/thriving",
                "Proactive intervention success"
            ]
        })
        
        for _, row in health_df.iterrows():
            st.markdown(f"""
            <div style='padding: 15px; background: #F9FAFB; border-radius: 4px; margin: 10px 0;
                        border: 1px solid #E5E5E5;'>
                <div style='font-weight: 600; color: #1F2937;'>{row['Metric']}</div>
                <div style='font-size: 32px; font-weight: 700; color: #1F2937; margin: 5px 0;'>{row['Target']}</div>
                <div style='color: #64748b; font-size: 14px;'>{row['Description']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# ========== ROADMAP TAB ==========
with tabs[4]:
    st.header("Implementation Roadmap")
    
    roadmap = [
        {
            "quarter": "Q1 2026",
            "focus": "Foundation & Core Integrations",
            "progress": 0,
            "deliverables": [
                "Hightouch Reverse ETL setup",
                "Amplitude product analytics implementation",
                "Salesforce sync configuration"
            ],
            "dependencies": [
                "Data engineering team",
                "Salesforce admin access",
                "Warehouse access permissions"
            ]
        },
        {
            "quarter": "Q2 2026",
            "focus": "Behavioral Automation & Segmentation",
            "progress": 0,
            "deliverables": [
                "Amplitude cohort models",
                "Automated email sequences via Hightouch",
                "Clay enrichment workflows",
                "Onboarding dashboard"
            ],
            "dependencies": [
                "Marketing ops team",
                "Product analytics data models",
                "Email platform configuration"
            ]
        },
        {
            "quarter": "Q3 2026",
            "focus": "Advanced Personalization Playbooks",
            "progress": 0,
            "deliverables": [
                "Developer-led growth playbook (Amplitude-triggered)",
                "Executive sponsorship playbook",
                "Usage-based health scoring",
                "Real-time personalization engine"
            ],
            "dependencies": [
                "Customer success input",
                "Amplitude behavioral models",
                "Hightouch sync templates"
            ]
        },
        {
            "quarter": "Q4 2026",
            "focus": "AI-Powered Optimization & Scale",
            "progress": 0,
            "deliverables": [
                "AI-powered next-best-action",
                "Predictive churn models (Amplitude + Databricks)",
                "Expansion recommendation engine",
                "Multi-team orchestration"
            ],
            "dependencies": [
                "ML engineering support",
                "Historical usage data",
                "Hightouch AI Decisioning"
            ]
        }
    ]
    
    for phase in roadmap:
        st.markdown(f"""
        <div style='background: white; padding: 25px; border-radius: 4px; 
                    margin: 20px 0; border: 2px solid #E5E5E5;
                    border-left: 4px solid #1F2937;'>
            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;'>
                <h3 style='margin: 0; color: #1F2937; font-weight: 600;'>{phase['quarter']}</h3>
                <span style='background: #1F2937; color: white; padding: 8px 16px; 
                            border-radius: 2px; font-weight: 600;'>{phase['focus']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📦 Deliverables:**")
            for deliverable in phase['deliverables']:
                st.markdown(f"✓ {deliverable}")
        
        with col2:
            st.markdown("**🔗 Dependencies:**")
            for dependency in phase['dependencies']:
                st.markdown(f"→ {dependency}")
        
        st.progress(phase['progress'] / 100)
    
    st.markdown("---")
    
    st.markdown("""
    <div style='background: #1F2937; padding: 30px; border-radius: 4px; margin-top: 20px;
                border: 2px solid #1F2937;'>
        <h2 style='color: white; margin-bottom: 20px; font-weight: 600;'>➡️ Next Steps</h2>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px;'>
            <div style='background: white; padding: 20px; border-radius: 4px;
                        border: 1px solid #E5E5E5;'>
                <h4 style='color: #1F2937; margin-bottom: 10px; font-weight: 600;'>1. Stakeholder Alignment</h4>
                <p style='color: #6B7280; margin: 0;'>Workshop with Sales, CS, Product, Engineering teams</p>
            </div>
            <div style='background: white; padding: 20px; border-radius: 4px;
                        border: 1px solid #E5E5E5;'>
                <h4 style='color: #1F2937; margin-bottom: 10px; font-weight: 600;'>2. Data Audit</h4>
                <p style='color: #6B7280; margin: 0;'>Validate current integrations and identify dependencies</p>
            </div>
            <div style='background: white; padding: 20px; border-radius: 4px;
                        border: 1px solid #E5E5E5;'>
                <h4 style='color: #1F2937; margin-bottom: 10px; font-weight: 600;'>3. Pilot Program</h4>
                <p style='color: #6B7280; margin: 0;'>Select 5-10 enterprise accounts for beta testing</p>
            </div>
            <div style='background: white; padding: 20px; border-radius: 4px;
                        border: 1px solid #E5E5E5;'>
                <h4 style='color: #1F2937; margin-bottom: 10px; font-weight: 600;'>4. Resource Planning</h4>
                <p style='color: #6B7280; margin: 0;'>Align for Q1 2026 implementation</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 20px;'>
    <p style='font-style: italic;'>Want to learn more? Email <a href=”mailto:jessi@jessijaramillo.com” target="_blank">jessi@jessijaramillo.com</a>.</p>
</div>
""", unsafe_allow_html=True)
