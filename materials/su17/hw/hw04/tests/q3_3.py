test = {
  'name': 'Question 3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 25 < len(missing) < 35
          True
          >>> 14 in missing
          True
          >>> 85 in missing
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(missing) == 30 and sum(missing) == 5272
          True
          """,
          'hidden': True,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
