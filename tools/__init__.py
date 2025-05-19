from .grammar import grammar_check
from .whisper import transcribe_and_analyze, translate
from .compareSentence import compare_sentence_mismatch, compare_sentence_word_level

TOOL_HANDLERS = {
    "grammar_check": grammar_check,
    "transcribe_and_analyze": transcribe_and_analyze,
    "translate": translate,
    "compareSentence": compare_sentence_mismatch,
    "compare_sentence_levenshtein":compare_sentence_word_level,
}