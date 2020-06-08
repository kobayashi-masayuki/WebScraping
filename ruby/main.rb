require 'rblineprof'
require 'rblineprof-report'

# すべてのRubyファイルを対象にする (gemなども計測される)
# target = /./

# カレントディレクトリ以下のRubyファイルを対象にする
target = /#{Dir.pwd}\/./

profile = lineprof(target) do
  require './script/fast_method.rb'
  require './script/slow_method.rb'

  fast
  slow
end
LineProf.report(profile)