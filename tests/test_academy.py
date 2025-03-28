import pytest
import utils


@pytest.mark.parametrize(
    "script_loc",
    [
        "./developers/academy/units/_snippets/setup.py",
        "./developers/academy/units/103_schema_and_imports/_snippets/05_create_instance.py",
        "./developers/academy/units/103_schema_and_imports/_snippets/20_schema.py",
        "./developers/academy/units/103_schema_and_imports/_snippets/30_import.py",
        "./developers/academy/units/103_schema_and_imports/_snippets/40_import_example_1.py",
    ],
)
def test_against_empty_weaviate(empty_weaviates, script_loc):
    proc_script = utils.load_and_prep_script(script_loc)
    exec(proc_script)


@pytest.mark.parametrize(
    "script_loc",
    [
        "./developers/academy/units/104_queries_2/_snippets/10_bm25.py",
        "./developers/academy/units/104_queries_2/_snippets/20_hybrid.py",
        "./developers/academy/units/104_queries_2/_snippets/30_generative.py",
        "./developers/academy/units/104_queries_2/_snippets/40_qna.py",
    ],
)
def test_against_edu_demo(empty_weaviates, script_loc):
    temp_proc_script_loc = utils.load_and_prep_temp_file(
        script_loc,
        lang="py",
        custom_replace_pairs=utils.edu_readonly_replacements
    )
    exec(temp_proc_script_loc.read_text())
