class Hoge
    def initialize
        @integers = (0..10000).to_a
    end

    def random_integer
        @integers.sample
    end
end

@hoge = Hoge.new

def slow
    10000.times do
        @hoge.random_integer
    end
end

