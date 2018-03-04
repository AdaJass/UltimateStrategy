## Data Structure Definition:
```
raw_data=
{
'code_period_ramdomStr': [data]
}

primary_data=
[
    {
        data: 'raw_data index'
        mirror_data: 'raw_data index'
        start_index: {
            pattern_index: [ ...]
        }
        des: ''
    }
]

mature_data=
{
    pattern_index: [  # the n_th unit's infomation
        {
            data: 'raw_data index'
            mirror_data: 'raw_data index'
            start: 0
            des: 
        }
    ]
}

pattern_repeats=
{
    pattern_index:[ #the n_th unit's same pattern
        {
            data: [('raw_data index', start_index), ....]
            flurmethod: [{'method': parameters} , ...]
            stable: 0.7
        }
    ]
}
```