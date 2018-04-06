/*
A KBase module: simple2
*/

module simple2 {
    /*
        Insert your typespec information here.
    */
    typedef structure {
        int base_number;
        string workspace_name;
    } SimpleParams;

    typedef structure {
        int new_number;
    } SimpleResults;

    funcdef simple_add(SimpleParams params)
        returns (SimpleResults output) authentication required;

};
