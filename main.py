import argparse
from pathlib import Path
from workingcal import get_working_calendar, save_working_calendar, input_validation_year, this_year


help_text = {
    'years': 'Enter years to download',
    'range': 'Enter the start and end year for downloading all data',
    'path': 'Enter the path to save the files'
}

parser = argparse.ArgumentParser()
parser.add_argument('--years', nargs='+', type=input_validation_year, default=this_year, help=help_text['years'])
parser.add_argument('--range', nargs='+', type=input_validation_year, default=False, help=help_text['range'])
parser.add_argument('--path', type=str, default='data', help=help_text['path'])
args = parser.parse_args()

out_path = Path(args.path)
True if out_path.is_dir() else out_path.mkdir()


if args.range:
    if len(args.range) == 2:
        start_year = int(min(args.range))
        end_year = int(max(args.range))
        years = range(start_year, end_year+1)

        for year in years:
            working_calendar = get_working_calendar(year)
            file_path = out_path / f'{year}.json'
            save_working_calendar(data=working_calendar, path=file_path)
    else:
        raise ValueError('Must enter 2 years')

else:
    try:
        for year in args.years:
            working_calendar = get_working_calendar(year)
            file_path = out_path / f'{year}.json'
            save_working_calendar(data=working_calendar, path=file_path)

    except:
        working_calendar = get_working_calendar(args.years)
        file_path = out_path / f'{args.years}.json'
        save_working_calendar(data=working_calendar, path=file_path)