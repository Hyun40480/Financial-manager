import streamlit as st
import pandas as pd
import numpy as np

# 1. 모바일 브라우저 최적화 설정 (앱 타이틀 및 레이아웃)
st.set_page_config(
    page_title="My Financial Manager",
    page_icon="📈",
    layout="centered",  # 모바일 세로 화면을 위해 centered 레이아웃 사용
    initial_sidebar_state="collapsed"  # 모바일에서 사이드바가 화면을 가리지 않도록 숨김
)

# 모바일 가독성을 위한 커스텀 스타일 CSS
st.markdown("""
    <style>
    /* 메트릭 카드 디자인 개선 (글자 크기 및 여백 조정) */
    [data-testid="stMetricValue"] {
        font-size: 24px !important;
        font-weight: bold;
    }
    /* 버튼 터치 영역 확대 */
    .stButton>button {
        width: 100%;
        height: 45px;
        font-size: 16px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📱 Financial Manager")
st.caption("실시간 미·국장 이슈 및 투기과열 모니터링")

# 2. 업데이트 버튼 (수동 새로고침 시뮬레이션)
if st.button("🔄 현재 시장 데이터 분석 및 업데이트"):
    with st.spinner("최신 뉴스 및 지표 분석 중..."):
        # 실제 구현 시 여기에 수집 및 LLM 분석 로직이 들어갑니다.
        st.success("업데이트 완료! (방금 전)")

st.write("---")

# 3. 큰 그림 (Main Dashboard) - 모바일 스크롤 최소화를 위한 탭 구조
# 스마트폰에서 한 손으로 탭을 눌러 시장을 전환할 수 있습니다.
tab_global, tab_kr, tab_us = st.tabs(["🌐 종합 요약", "🇰🇷 한국 시장", "🇺🇸 미국 시장"])

# ----------------- [탭 1: 종합 요약] -----------------
with tab_global:
    st.subheader("🔥 오늘 종합 리포트")
    st.info("현재 시장은 **AI 및 반도체** 분야로 수급이 극단적으로 쏠려 있습니다. 국장은 다소 침체되어 있으나 미장은 과열 신호가 감지됩니다.")
    
    # 주요 지표 카드 배치 (모바일에서는 자동으로 세로 정렬되거나 압축됨)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="코스피 상태", value="🚨 과열 주의", delta="점수: 78/100")
    with col2:
        st.metric(label="나스닥 상태", value="😱 극단적 탐욕", delta="점수: 89/100")

# ----------------- [탭 2: 한국 시장 상세] -----------------
with tab_kr:
    st.subheader("🇰🇷 국장 과열 진단 및 테마")
    
    # 1. 과열 지표 요약
    st.markdown("### 📊 핵심 과열 지표")
    st.metric(label="신용융자 잔고 비율", value="5.4% (위험)", delta="전일 대비 +0.2%")
    st.metric(label="거래대금 회전율", value="240% (폭발)", delta="최근 5일 평균 대비 1.5배")
    
    # 2. 집중 이슈 상세 분석
    st.markdown("### 🔍 실시간 집중 이슈 (AI 분석)")
    with st.expander("1. 초전도체/신소재 테마 수급 급증"):
        st.write("""
        - **과열 판단:** **위험 (투기성 강함)**
        - **이유:** 실질적인 매출 실적 없이 커뮤니티(리포트) 버즈량만으로 거래량이 폭발하고 있음. 20일 이격도가 125%를 초과하여 단기 급락 위험 존재.
        """)
    with st.expander("2. K-뷰티/화장품 수출 호조"):
        st.write("""
        - **과열 판단:** **양호 (실적 기반)**
        - **이유:** 기관/외인 동반 순매수 유입 중. 실용적인 수출 데이터가 뒷받침되어 고평가 논란이 적음.
        """)

# ----------------- [탭 3: 미국 시장 상세] -----------------
with tab_us:
    st.subheader("🇺🇸 미장 과열 진단 및 테마")
    
    st.markdown("### 📊 핵심 과열 지표")
    st.metric(label="CNN Fear & Greed", value="82 (Extreme Greed)", delta="지난주: 75")
    st.metric(label="RSI 14 (빅테크 평균)", value="76.5 (과매수)", delta="기준점 70 초과")
    
    st.markdown("### 🔍 실시간 집중 이슈 (AI 분석)")
    with st.expander("1. 빅테크 AI 인프라 추가 지출"):
        st.write("""
        - **과열 판단:** **주의 (고평가 구간)**
        - **이유:** AI 칩셋 수요는 여전하나 엔비디아를 비롯한 주요 반도체 주가들이 60일 이동평균선과 격차를 크게 벌림. 추격 매수는 불리한 구간.
        """)
    with st.expander("2. 레디딧(WSB) 밈 주식 폭등"):
        st.write("""
        - **과열 판단:** **극단적 투기 (진입 금지)**
        - **이유:** 특정 숏스퀴즈 기대 종목의 옵션 거래량이 전일 대비 800% 폭증. 펀더멘탈 무관한 단기 머니게임 양상.
        """)