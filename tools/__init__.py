from .grammar import grammar_check
from .vocab import vocab_suggest
from .logic import logic_review
from .whisper import transcribe_and_analyze, translate
from .compareSentence import compare_sentence_mismatch

TOOL_HANDLERS = {
    "grammar_check": grammar_check,
    "vocab_suggest": vocab_suggest,
    "logic_review": logic_review,
    "transcribe_and_analyze": transcribe_and_analyze,
    "translate": translate,
    "compareSentence": compare_sentence_mismatch,
}