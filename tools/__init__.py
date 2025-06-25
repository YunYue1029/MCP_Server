from .grammar import grammar_check
from .whisper import transcribe_and_analyze, translate
from .compareSentence import compare_sentence_word_level
from .final_ouput import final_output
from .pridict_speech import predict_speech

TOOL_HANDLERS = {
    "grammar_check": grammar_check,
    "transcribe_and_analyze": transcribe_and_analyze,
    "translate": translate,
    "compare_sentence_levenshtein":compare_sentence_word_level,
    "final_output": final_output,
    "predict_speech": predict_speech,
}