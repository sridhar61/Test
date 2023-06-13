import argparse
import dial_the_inspector_v3

def get_inspector_results(applicationid):
    type_of_inspection = "tags"
    path_to_local_creds = "path/to/local/creds"
    vendor = "datadog"
    xray = False

    inspector_results, fidol_tags_datadog = dial_the_inspector_v3.fidol_inspector(
        applicationid, type_of_inspection, path_to_local_creds, vendor, xray
    )

    return inspector_results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments needed for successful execution')
    parser.add_argument('-a', '--applicationid', help='Application ID number', required=True)
    args = parser.parse_args()
    results = get_inspector_results(args.applicationid)
    print(results)
