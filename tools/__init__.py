from .grammar import grammar_check
from .whisper import transcribe_and_analyze, translate
from .compareSentence import compare_sentence_mismatch

TOOL_HANDLERS = {
    "grammar_check": grammar_check,
    "transcribe_and_analyze": transcribe_and_analyze,
    "translate": translate,
    "compareSentence": compare_sentence_mismatch,
}