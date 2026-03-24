from mylib.logic import gemini

def test_gemini():
    result = gemini("what is the capital of France?")
    assert "Paris" in result

# assert is used to check if the expected output is in the result returned by the gemini function.