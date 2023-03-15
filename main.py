import streamlit as st


class Exercise:
    def __init__(self, name):
        self.name = name
        self.score = 0.0
        self.max_score = 1.0

    def ui(self):
        with st.container():
            colempty, colbody = st.columns([1, 16])
            with colempty:
                st.empty()
            with colbody:
                with st.container():
                    st.subheader(self.name)
                    col0, col1, col2 = st.columns([1, 4, 4])
                    with col0:
                        st.empty()
                    with col1:
                        self.score = st.number_input('Score', key=self.name+"score")
                    with col2:
                        self.max_score = st.number_input('Maximum score', min_value=0.01, value=self.max_score, key=self.name+"max")
                    if self.score > self.max_score:
                        st.warning("Make sure the score is lower than the maximum.", icon="⚠️")


def calculate_percentage(score, maxscore):
    return calculate_custom_max(score, maxscore, 100)


def calculate_custom_max(score, maxscore, newmax):
    return score / maxscore * newmax


class Test:
    def __init__(self):
        if 'elements' not in st.session_state:
            st.session_state.elements = []
        self.elements = st.session_state.elements

    def add_group(self, group):
        self.elements.append(group)

    def calculate_total(self):
        tot = 0.0
        for group in self.elements:
            tot = tot + group.score
        return tot

    def calculate_max(self):
        tot = 0.0
        for group in self.elements:
            tot = tot + group.max_score
        return tot

    def ui(self):
        if st.button("Add exercise"):
            e = Exercise(f"Exercise {len(self.elements) + 1}:")
            self.add_group(e)
        st.title("Exercises")
        for group in self.elements:
            group.ui()
        if self.elements:
            st.title("Results")
            score = self.calculate_total()
            max_score = self.calculate_max()
            perc = calculate_percentage(score, max_score)
            col_left, col_right = st.columns(2)
            with col_left:
                st.markdown(f"#### Score: {score} / {max_score}")
            with col_right:
                st.markdown(f"#### {perc}%")
            if st.checkbox("Change the maximum score?"):
                custom_max_score = st.number_input("New maximum score", value=max_score, min_value=0.01)
                custom_score = calculate_custom_max(score, max_score, custom_max_score)
                st.markdown(f"#### Custom score: {custom_score} / {custom_max_score}")


if __name__ == '__main__':
    test = Test()
    test.ui()
