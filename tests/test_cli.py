from hello_streamlit2.cli import parse_args


def test_parse_args():
    # Test case 1: No arguments provided
    args = parse_args([])
    assert args.port == 18501

    # Test case 2: Port argument provided
    args = parse_args(["-p", "8080"])
    assert args.port == 8080

    # Test case 3: Invalid port argument provided
    try:
        parse_args(["-p", "abc"])
    except SystemExit:
        pass
    else:
        assert False, "Expected SystemExit exception"

    # Test case 4: Help argument provided
    try:
        parse_args(["-h"])
    except SystemExit:
        pass
    else:
        assert False, "Expected SystemExit exception"
