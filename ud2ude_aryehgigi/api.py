from .conllu_wrapper import parse_conllu, serialize_conllu, parse_odin, conllu_to_odin, parsed_tacred_json
from .converter import convert


def convert_ud2ude_conllu(conllu_text, enhance_ud=True, enhanced_plus_plus=True, enhanced_extra=True, preserve_comments=False, conv_iterations=1, remove_eud_info=False, remove_extra_info=False):
    parsed, all_comments = parse_conllu(conllu_text)
    converted, _ = convert(parsed, enhance_ud, enhanced_plus_plus, enhanced_extra, conv_iterations, remove_eud_info, remove_extra_info)
    return serialize_conllu(converted, all_comments, preserve_comments)


def convert_ud2ude_odin(odin_json, enhance_ud=True, enhanced_plus_plus=True, enhanced_extra=True, conv_iterations=1, remove_eud_info=False, remove_extra_info=False):
    sents = parse_odin(odin_json)
    converted_sents, _ = convert(sents, enhance_ud, enhanced_plus_plus, enhanced_extra, conv_iterations, remove_eud_info, remove_extra_info)
    converted_odin = conllu_to_odin(converted_sents, False, odin_json)
    
    return converted_odin


def convert_ud2ude_tacred(tacred_json, enhance_ud=True, enhanced_plus_plus=True, enhanced_extra=True, conv_iterations=1, remove_eud_info=False, remove_extra_info=False):
    sents = parsed_tacred_json(tacred_json)
    converted_sents, _ = convert(sents, enhance_ud, enhanced_plus_plus, enhanced_extra, conv_iterations, remove_eud_info, remove_extra_info)
    
    return converted_sents

