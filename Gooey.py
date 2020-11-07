from gooey import Gooey, GooeyParser

@Gooey(program_name='FBLA Quiz')
def main():
    parser = GooeyParser()

    group1 = parser.add_argument_group('Question 1')
    mcq = group1.add_mutually_exclusive_group()
    mcq.add_argument('-a', '--Option A', action="store_true")
    mcq.add_argument('-b', '--Option B', action="store_true")

    group2 = parser.add_argument_group('Question 2')
    group2.add_argument("Type in the missing word: 'FBLA is ___'", action="store")
 
    group3 = parser.add_argument_group('T/F: FBLA is goated')
    tf = group3.add_mutually_exclusive_group()
    tf.add_argument('-t', '--True', action="store_true")
    tf.add_argument('-f', '--False', action="store_true")

    group4 = parser.add_argument_group('Question 4')

    args=parser.parse_args()

    print(vars(args))

main()